"""Modules to collect metadata for Arya sourced candidates"""
# -*- coding: utf-8 -*-
# @author Ratnadip Adhikari

from __future__ import absolute_import
import sys
import os
import re
import logging
import pandas as pd
# +++++++++++++++++
BASE_PATH = os.path.abspath("./arya-helpers/Codes/src")
extendPaths = [p for p in (os.path.dirname(BASE_PATH), BASE_PATH) if p not in sys.path]
sys.path = extendPaths + sys.path
# +++++++++++++++++
from collections import Counter
from itertools import groupby
from operator import itemgetter
from functools import reduce
from joblib import Parallel, delayed
from aryautils.storageutils import MySQLManager
from aryahelpers.utils.mysqlutils import MySQLHelpers
from aryahelpers.aryatestbed.explaccess import AccessExplanations
from aryahelpers.appconfig import CONFIG, CANDIDATE_TABLES, JOB_METADATA_COLS, SOURCED_CONTDS_COLS
from aryahelpers.utils.genericutils import elapsedTime, null_handler, merge_dicts, flatten_iterable, save_files
LOGGER = logging.getLogger(__name__)


class AryaSourcedContenders():
    """Class for extracting Arya sourced contenders details"""
    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]
        self.expl_key = 'ExplanationFacts'
        self.db_name, self.toprocess_tbl, self.jobid_key, self.guid_key = tuple(
            CANDIDATE_TABLES["toprocess"]["base"].values())[1:]
        
    @staticmethod
    def get_dbkey(env: str):
        """Return db key for the source env"""
        if env == 'qa':
            return 'database'
        return f'database.{env}'
    
    def _extract_given_exp(self, job_id: int):
        """Extract min & max experience for the given job from the `intel`.`experience` table"""
        query_str = f"SELECT * FROM experience WHERE JobId={job_id};"
        query_res = MySQLManager.execute_query(query_str, (), **CONFIG[self.db_key]['intel'])
        if not query_res:
            return
        return (query_res[0]['min'], query_res[0]['max'], query_res[0]['source'])
    
    def _get_contd_skills(self):
        """Get contender skills info -- MATCHED, TRAINABLE, MISSING"""
        skills_info = {}
        skill_keys = ['Matched', 'Missing', 'Trainable']
        for idx, jid in enumerate(self.job_ids):
            contd_skills = []      
            accessor = AccessExplanations(
                job_id=jid, num_candidates=None, candidate_name=None, candidate_guid=None,
                recommendation_status_id=None, explanation_type='skill', base_env=self.source_env
            )
            response_json = accessor.access_explanations()[:self.top_contds]
            contd_skills = [merge_dicts(({"CandidateGuid": expl_val for ek, expl_val in expl_dict.items() \
                if 'guid' in ek.lower()}, {f"{sk+'Skills'}": v[sk]['Skills'] for sk in v if sk in skill_keys})) \
                    for expl_dict in response_json for k, v in expl_dict.items() if k.lower() == 'explanation']
            skills_info.update({jid: contd_skills})
        return skills_info

    def _get_info_from_expl(self, expl_dict: dict, skills_info: dict, job_id: int):
        """Get the available (non-null) facts keys for a given eplanation dict"""
        info_from_expl = {}
        facts_dict = {self.expl_key: {re.sub(r'[^a-zA-Z]+', '', _fk): _fact for _fk, _fact in v[
            self.expl_key].items() if _fact} for k, v in expl_dict.items() if k.lower() == 'explanation'}
        info_from_expl = {"CandidateGuid" if 'guid' in k.lower() else k: v for k, v in expl_dict.items() if any(
            s in k.lower() for s in ('name', 'score', 'guid'))}
        for idx, skills_dict in enumerate(skills_info[job_id]):
            if skills_dict["CandidateGuid"] == info_from_expl["CandidateGuid"]:
                info_from_expl.update(skills_dict)
                break
        all_factkeys = list(facts_dict.get(self.expl_key).keys())
        info_from_expl.update(merge_dicts(({"GeneratedExplanations": all_factkeys}, facts_dict)))
        return info_from_expl
    
    def _extract_toprocess_info(self, job_id: int, source_guids: tuple):
        query_str = f"SELECT {self.jobid_key} AS JobId, portal_candidate_id AS CandidateGuid, name AS CandidateName, \
            title AS CurrentTitle, company AS CurrentCompany, highest_degree AS HighestDegree, \
                industry AS CandidateIndustry, location AS CandidateLocation, total_experience + 0.0 AS \
                    TotalExperince, IF(resume_content IS NULL, FALSE, TRUE) as HasResume FROM {self.toprocess_tbl} \
                        WHERE {self.jobid_key}={job_id} AND {self.guid_key} in {source_guids};"
        return MySQLManager.execute_query(query_str, (), **CONFIG[self.db_key][self.db_name])
    
    def _create_groupcontds_df(self, arya_groupcontds: dict):
        """Creates a unified dataframe of Arya same conteders groups.
        The param: `arya_groupcontds` is a dict of individual group dataframes"""
        all_groups = list(arya_groupcontds.keys())
        if not all_groups:
            return
        group_cols = ['GroupName'] + list(arya_groupcontds[all_groups[0]])
        groupcontds_df, empty_df = pd.DataFrame(columns=group_cols), pd.DataFrame(index=[0], columns=group_cols)
        # Join individual groups
        for i in range(len(all_groups)):
            curr_group = arya_groupcontds[all_groups[i]]
            aux_group_df = pd.DataFrame([f'group-{i}']*len(curr_group), columns=['GroupName'])
            curr_group = pd.concat([aux_group_df, curr_group], axis=1, sort=False)
            groupcontds_df = pd.concat([groupcontds_df, curr_group, empty_df], ignore_index=True)
        return groupcontds_df
    
    def _collect_jobs_metadata(self):
        """Collect metadata info for the provided jobs"""
        jobs_metadata = {}
        job_details = Parallel(n_jobs=-1)(delayed(MySQLHelpers.extract_arya_jobdetails)(self.db_key, jid) for jid in self.job_ids)
        jobs_exps = Parallel(n_jobs=-1)(delayed(self._extract_given_exp)(jid) for jid in self.job_ids)
        for idx, jid in enumerate(self.job_ids):
            try:
                metadata_info = {k: v for k, v in job_details[idx].items() if k in JOB_METADATA_COLS}
                metadata_info = merge_dicts(({"JobId": jid}, metadata_info, {"JobExperience": jobs_exps[idx]}))
                jobs_metadata.update({jid: metadata_info})
            except Exception as error:
                LOGGER.error(error)
                LOGGER.info("Error in extracting metadata info for the job: %s", jid)
        self.jobs_metadata = jobs_metadata
        
    def _collect_contds_metadata(self):
        """Collect sourced contenders details for the given jobs"""
        contds_metadata, guids_map = {}, {}
        try:
            skills_info = self._get_contd_skills()  # get contds skills info for all jobs
            for idx, jid in enumerate(self.job_ids):
                metadata_info = []
                # Access candidates explanations for given jobid
                accessor = AccessExplanations(
                    job_id=jid, num_candidates=None, candidate_name=None, candidate_guid=None,
                    recommendation_status_id=None, explanation_type='facts', base_env=self.source_env
                )
                response_json = accessor.access_explanations()[:self.top_contds]
                [metadata_info.append(self._get_info_from_expl(expl_dict, skills_info, jid)) 
                 for idx, expl_dict in enumerate(response_json)]
                guids_map[jid] = tuple([d["CandidateGuid"] for d in metadata_info])
                contds_metadata.update({(jid, d["CandidateGuid"]): d for d in metadata_info})
            # Extract contds info from toprocess table
            args_list = [(jid, guids_map[jid]) for jid in self.job_ids if guids_map[jid]]
            toprocess_info = Parallel(n_jobs=-1)(delayed(self._extract_toprocess_info)(*args) for args in args_list)
            toprocess_info = flatten_iterable(toprocess_info)
            toprocess_info = {(d["JobId"], d["CandidateGuid"]): d for d in toprocess_info}
            contds_metadata = {_key: merge_dicts((toprocess_info.get(_key, {}), _info)) 
                               for _key, _info in contds_metadata.items()}   # associate collected info
        except Exception as error:
            LOGGER.error(error)
            LOGGER.info("Unexpected Error in extracting contds metadata info")
        self.contds_metadata = contds_metadata
        
    def derive_sourcedcontds_count(self):
        """Derive jobwise sourced contenders stats"""
        contdscount_dict = dict(Counter([d["JobId"] for ix, d in enumerate(self.arya_sourcedcontds)]))
        self.contds_count = {jid: f"Accessed candidates: {contdscount_dict.get(jid, 0)}" for jid in self.job_ids}

    @elapsedTime
    def access_contdsinfo(self, save_path=False, save_type='.json'):
        """Create metadata (jobs & contds) for explanation quality analysis.
        The param: `save_type` can be `'.json'` or `'.xlsx'`.
        """
        self.job_ids = sorted(self.job_ids, reverse=True) if self.to_sort else self.job_ids
        self.top_contds = null_handler(self.top_contds, 300)
        self.db_key = self.get_dbkey(self.source_env)
        self.arya_sourcedcontds = []
        try:
            self._collect_jobs_metadata()  # collect jobs metadata
            self._collect_contds_metadata()  # collect contds metadata
            [self.arya_sourcedcontds.append(merge_dicts((self.jobs_metadata[_key[0]], _info))) 
             for _key, _info in self.contds_metadata.items()]
            self.derive_sourcedcontds_count()
            # Save the created metadata as '.json' or '.xlsx' file
            save_metadata = self.arya_sourcedcontds if save_type == '.json' else pd.DataFrame([
                {k: v for k, v in d.items() if k != self.expl_key} for idx, d in enumerate(
                    self.arya_sourcedcontds)], columns=SOURCED_CONTDS_COLS)
            save_files(save_metadata, save_path, 'arya_sourcedcontds', save_type,
                       indent=4, index=False, freeze_panes=(1, 0))            
        except Exception as error:
            LOGGER.error(error)
            LOGGER.error("Unexpected Error in creating explanations quality metadata !!")
            raise error
    
    @elapsedTime
    def group_samecontdsinfo(self, save_path=False, save_type='.json'):
        """Collect info of same contenders, sourced into nultiple jobs"""
        self.arya_groupcontds = {}
        self.groupcontds_count = {}
        try:
            seg_jobs, sourced_contds, common_guids = {"qa": [], "staging": [], "prod": []}, [], {}
            [seg_jobs[env].append(jid) for ix, jinfo in enumerate(self.jobs_info) for env, jid in jinfo.items()]
            for env in seg_jobs:
                sourced_obj = AryaSourcedContenders(
                    source_env=env, job_ids=seg_jobs[env], top_contds=self.top_contds, to_sort=False)
                sourced_obj.access_contdsinfo()
                sourced_contds.extend(sourced_obj.arya_sourcedcontds)
            for ix, jobs_dict in enumerate(self.jobs_info):
                gname = f"group-{ix}"
                group_jobids, self.arya_groupcontds[gname] = list(jobs_dict.values()), []
                guids_dict = {jid: set() for jid in group_jobids}
                [guids_dict[jid].add(contd_dict.get('CandidateGuid')) for env, jid in jobs_dict.items()
                 for idx, contd_dict in enumerate(sourced_contds) if contd_dict.get('JobId') == jid]
                common_guids[gname] = list(reduce(lambda x, y: x & y, guids_dict.values()))
                subset_contds = [contd_dict for idx, contd_dict in enumerate(sourced_contds) if (contd_dict.get(
                    'JobId') in group_jobids) and (contd_dict.get('CandidateGuid') in common_guids[gname])]
                subset_contds = sorted(subset_contds, key=itemgetter('CandidateGuid'))     
                [self.arya_groupcontds[gname].extend(list(g)) for i, g in groupby(
                    subset_contds, key=itemgetter('CandidateGuid'))]
            # Count group of contenders for each group
            self.groupcontds_count = {k: f"{len(common_guids[k])} same contenders sourced for these jobs"
                                      for k in self.arya_groupcontds}
            # Save the grouped contenders details as '.json' or '.xlsx'
            save_data = self.arya_groupcontds
            if save_type == '.xlsx':
                save_data = {_gname: pd.DataFrame(
                    [{k: v for k, v in d.items() if k != self.expl_key} for idx, d in enumerate(_group)],
                    columns=SOURCED_CONTDS_COLS) for _gname, _group in save_data.items() if _group
                }
                save_data = self._create_groupcontds_df(save_data)
            save_files(save_data, save_path, 'arya_groupcontds', save_type, indent=4, index=False, freeze_panes=(1, 0))
        except Exception as error:
            LOGGER.error(error)
            LOGGER.error("Unexpected Error in creating groups of same contenders !!")
            raise error
    

if __name__ == '__main__':
    print('python version:', sys.version)   
    print('cwd:', os.getcwd())
