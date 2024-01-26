"""Modules to access candidates explanations from DB"""
# -*- coding: utf-8 -*-
# @author Ratnadip Adhikari

import sys, os, json
BASE_PATH = os.path.abspath("./arya-helpers/Codes/src")
extendPaths = [p for p in (os.path.dirname(BASE_PATH), BASE_PATH) if p not in sys.path]
sys.path = extendPaths + sys.path
from copy import deepcopy
from aryautils.storageutils import MySQLManager
from aryahelpers.utils.mysqlutils import MySQLHelpers
from aryahelpers.appconfig import CONFIG, ALL_FEATURES, FACT_TOKENS, CANDIDATE_TABLES
from aryahelpers.utils.genericutils import merge_dicts, flatten_iterable
import logging
LOGGER = logging.getLogger(__name__)


class AccessExplanations(object):
    """Access candidates explanations from DB"""
    def __init__(self, **kwargs):
        self._ALL_FEATURES = set(k.lower() for k in ALL_FEATURES)
        [setattr(self, k, v) for k, v in kwargs.items()]
        # job_id, num_candidates, candidate_name, candidate_guid
    
    def get_explanation_facts(self, candidate_details: dict):
        """Filter explanations, based on `explanation_type`"""
        explanation_type = self.explanation_type  # 'company', 'skill', 'role', 'occupation',
                                                  # 'industry', 'experience', 'facts'
        filtered_explanations = {}
        if explanation_type:
            if explanation_type != 'facts':
                filtered_explanations = candidate_details.get(
                    explanation_type, candidate_details.get(explanation_type.title(), {}))
            else:
                all_explkeys = list(candidate_details.keys())
                all_explkeys = {k: k if k.lower() != 'summary' else f'#{k}' for k in all_explkeys if isinstance(
                    candidate_details[k], dict) and (set(candidate_details[k].keys()) & FACT_TOKENS)}
                filtered_explanations["ExplanationFacts"] = {}
                for _explkey in all_explkeys:
                    for _fact_key in FACT_TOKENS:
                        get_facts = candidate_details.get(_explkey, {}).get(_fact_key, [])
                        if isinstance(get_facts, list):
                            get_facts = [_fact.get('Fact', '') + _fact.get('fact', '') if isinstance(
                                _fact, dict) else _fact for _fact in get_facts]
                        if get_facts:
                            filtered_explanations["ExplanationFacts"][all_explkeys[_explkey]] = get_facts
                            break
        else:
            return candidate_details
        return filtered_explanations
    
    def extract_analyzed_candidates(self, expl_tbl_key, job_id=None, expl_type=None):
        """Extract analyzed candidates details from the respective db"""
        cand_details = []
        db_key, db_name, table_name, jobid_key, contd_guid, expl_key = tuple(
            CANDIDATE_TABLES["explanation"][expl_tbl_key].values())
        # Add the respective Score
        score_keys = ["CandidateScore"]
        if expl_type in self._ALL_FEATURES:
            score_keys += [] if expl_type in ['facts', 'summary'] else [
                "{}Score".format(expl_type.title())] if expl_type != 'role' else ['RoleLevelScore']
        else:
            score_keys += ['CompanyScore', 'RoleLevelScore', 'OccupationScore', 'EducationScore',
                            'ExperienceScore', 'IndustryScore', 'SkillScore']
        query_str = "SELECT {}, {}, {}, CONVERT_TZ(UpdatedDateTime,'+00:00','+05:30') \
            AS UpdatedDateTime, {} FROM {} WHERE {}={}".format(
                jobid_key, ", ".join(score_keys), contd_guid, expl_key, table_name, jobid_key, job_id)
        cand_details = MySQLManager.execute_query(query_str, (), **CONFIG[db_key][db_name])
        cand_details = [{k: v for k, v in d.items() if v or (k not in score_keys)} for d in cand_details]
        for idx, d in enumerate(cand_details):
            cand_details[idx][expl_key] = deepcopy(json.loads(d[expl_key]))
            cand_details[idx][expl_key] = self.get_explanation_facts(cand_details[idx][expl_key])
        return cand_details
    
    def filter_candidates(self, contd_details: list, filter_keys: tuple):
        """Filter `contd_details` with respect to `filter_keys`"""
        filtered_details = contd_details.copy()
        num_candidates = self.num_candidates
        candidate_name = self.candidate_name
        candidate_guid = self.candidate_guid
        recommendation_status_id = self.recommendation_status_id  #[1, 2, 3]
        if num_candidates:
            filtered_details = [d for d in filtered_details[:num_candidates]]
        if candidate_name:
            filtered_details = [d for d in filtered_details if d[filter_keys[0]] == candidate_name]
        if candidate_guid:
            filtered_details = [d for d in filtered_details if d[filter_keys[1]] == candidate_guid]
        if recommendation_status_id:
            filtered_details = [d for d in filtered_details if d[filter_keys[2]] == recommendation_status_id]
        return filtered_details
    
    def access_explanations(self):
        """Access explanations, based on specific filtering conditions"""
        job_id, base_env = self.job_id, self.base_env
        explanation_type = self.explanation_type

        # Access candidates explanations and other details
        cand_explanations, filter_guids = [], []
        expl_tbl_key = 'qa-reservoir' if base_env == 'qa' else 'copy' if base_env == 'new' else base_env
        cand_details = self.extract_analyzed_candidates(expl_tbl_key, job_id, explanation_type)
        if not cand_details and (base_env in ['qa', 'new']):
            expl_tbl_key = 'qa-arya'
            cand_details = self.extract_analyzed_candidates(expl_tbl_key, job_id, explanation_type)
        
        # Filter cand_guids
        db_key, guid_key = [CANDIDATE_TABLES["explanation"][expl_tbl_key][k] for k in ('db_key', 'guid_key')]
        jtr_candidates = MySQLHelpers().get_TopN_JTR(db_key, job_id)
        if jtr_candidates:
            filter_guids = [(d['candidate_name'], d['portal_candidate_id'],
                             d['recommendation_status_id']) for d in jtr_candidates]
            filter_guids = self.filter_candidates(filter_guids, (0, 1, 2))
            # Access explanations
            for cand_info in filter_guids:
                subset_cands = [d for d in cand_details if d[guid_key] == cand_info[1]]
                if guid_key == 'portalGuid':
                    subset_cands = sorted(subset_cands, key=lambda d: d['UpdatedDateTime'], reverse=True)
                if subset_cands:
                    subset_cands = merge_dicts(({
                        "CandidateName": cand_info[0], "recommendation_status_id": cand_info[2]}, subset_cands[0]))
                    cand_explanations.append(subset_cands)
        else:
            # if jtr_candidates list is empty, e.g. manually entered info
            cand_details = [d for d in cand_details if d.get("CandidateScore", 0) >= 0]
            cand_details = sorted(cand_details, key=lambda x: x.get("CandidateScore", 0), reverse=True)
            cand_details = self.filter_candidates(cand_details, ('', guid_key, ''))
            cand_explanations.extend(cand_details)
        cand_explanations = flatten_iterable(cand_explanations)
        return cand_explanations
  

if __name__ == '__main__':
    print('python version:', sys.version)   
    print('cwd:', os.getcwd())
    # =================
    accessor = AccessExplanations(
        job_id=359228, num_candidates=10, candidate_name=None, candidate_guid=None,
        recommendation_status_id=None, explanation_type='facts', base_env='qa'
    )
    cand_explanations = accessor.access_explanations()
    print(json.dumps(cand_explanations, indent=4, default=str))
