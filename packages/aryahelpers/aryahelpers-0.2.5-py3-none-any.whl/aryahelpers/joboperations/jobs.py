"""Modules to peroform automated Arya job operationsB"""
# -*- coding: utf-8 -*-
# @author Ratnadip Adhikari

import sys
import os
import re
import requests
import base64
# +++++++++++++++++
BASE_PATH = os.path.abspath("./arya-helpers/Codes/src")
extendPaths = [p for p in (os.path.dirname(BASE_PATH), BASE_PATH) if p not in sys.path]
sys.path = extendPaths + sys.path
# +++++++++++++++++
from datetime import datetime
from joblib import Parallel, delayed
from aryautils.storageutils import MySQLManager
from aryahelpers.appconfig import CONFIG, COPY_JOB_LIMIT, CANDIDATE_TABLES
from aryahelpers.utils.genericutils import elapsedTime, merge_dicts, save_files
from aryahelpers.utils.mysqlutils import MySQLHelpers
import logging
LOGGER = logging.getLogger(__name__)


class AryaJobOperations():
    """Arya job operations class"""
    def __init__(self, **kwargs):
        [setattr(self, k, v) for k, v in kwargs.items()]
        self.db_name, self.base_table, self.jobid_key, self.guid_key = tuple(
            CANDIDATE_TABLES["toprocess"]["base"].values())[1:]
        self.copy_table = CANDIDATE_TABLES["toprocess"]["copy"]["table"]

    def _get_dbkey_and_joburl(self, env: str):
        """Get db_key and Arya job URL for the given environment ('qa' or 'staging')"""
        dbkey_for_env = 'database' if env == 'qa' else f'database.{env}'
        joburl_for_env = CONFIG['arya_job_urls']['jobs_v3.1']
        joburl_for_env = re.sub('<ENV>', f"-{env}" if env != 'prod' else '', joburl_for_env)
        return dbkey_for_env, joburl_for_env
    
    def validate_copy_jobs_payload(self, payload):
        """Validate the payload for copy jobs"""
        if payload:
            job_ids = payload.get('job_ids', [])
            source_and_target_envs = payload.get('source_and_target_envs', [])
            source_and_target_users = payload.get('source_and_target_users', [])
            users_lens_set = {len(source_and_target_envs), len(source_and_target_users)}
            if job_ids and len(job_ids) <= COPY_JOB_LIMIT and users_lens_set == {2}:
                if set(source_and_target_envs) <= {'qa', 'staging', 'prod'}:
                    self.job_ids = job_ids
                    self.source_env, self.target_env = source_and_target_envs
                    self.source_user_email, self.target_user_email = source_and_target_users
                    self.job_status_id = payload.get('target_jobs_status', 2)
                    self.to_retain_job = payload.get('to_retain_job', False)
                    self.source_db_key, self.source_job_url = self._get_dbkey_and_joburl(self.source_env)
                    self.target_db_key, self.target_job_url = self._get_dbkey_and_joburl(self.target_env)
                    return True
        return False
    
    @staticmethod
    def form_headers(user_email):
        """Form headers from `user_email`"""
        headers = {}
        bs4_email = base64.b64encode(user_email.encode('utf-8')).decode('utf-8')
        headers['Authorization'] = f"AryaKey {CONFIG['arya_api_auth']['application_id']};{CONFIG['arya_api_auth']['application_key']};{bs4_email}"
        headers['accept'] = "application/octet-stream"
        headers['Content-Type'] = "application/json"
        return headers

    def make_request(self, req_method, url, url_name=None, user_email=None, payload=None, headers=None):
        """Make GET/POST request"""
        if user_email:
            headers = AryaJobOperations.form_headers(user_email)
        request_resp = requests.get(url, json=payload, headers=headers) if req_method == 'GET' \
            else requests.post(url, json=payload, headers=headers)
        print(f'{url_name} response status code: {request_resp.status_code}')
        if not request_resp.content:
            return
        return request_resp.json()
    
    def copy_single_job(self, job_id):
        """Copy a single job from source to target user"""
        copyjob_info = {"source_job": job_id, "target_job": None}
        source_job = self.make_request('GET', f"{self.source_job_url}/{job_id}", 'GET JOB', self.source_user_email)
        if not source_job:
            return copyjob_info
        print(f'Fetched job: {job_id}')
        client_mapping = MySQLHelpers.fetch_or_add_client_for_user(
            self.target_db_key, source_job['Client'], self.target_user_email, 'user_email')
        if not client_mapping:
            return copyjob_info
        source_job['StatusId'], source_job['ClientId'], source_job['AssignedTo'] = \
            self.job_status_id, client_mapping['ClientID'], [self.USER['UserGuid']]
        target_job = self.make_request('POST', self.target_job_url, 'CREATE JOB', self.target_user_email, source_job)
        if target_job:
            target_job_id = target_job['JobId']
            if self.to_retain_job:
                MySQLHelpers.transact_to_jobsretain_tbl(
                    self.target_db_key, 'candidate_reservoir', [target_job_id], 'insert')
            print(f"Created job: {target_job_id}")
            copyjob_info = {"source_job": job_id, "target_job": target_job_id}
        return copyjob_info

    @elapsedTime    
    def copy_jobs_from_source_to_target(self, payload, is_validated=False):
        """Module for copying jobs from source user to target user"""
        self.copyjobs_info = []
        try:
            isvalid_payload = is_validated if is_validated else self.validate_copy_jobs_payload(payload)
            if isvalid_payload:
                self.USER = MySQLHelpers._get_user_info_from_db(self.target_db_key, self.target_user_email, 'user_email')
                self.USER = self.USER[0] if self.USER else {}
                self.copyjobs_info = [self.copy_single_job(jid) for jid in self.job_ids]
        except Exception as error:
            LOGGER.error('Failed in copying jobs from source to target user !')
            LOGGER.exception(error)

    def _filter_jobs_record(self, jobs_record: dict, filter_dict: dict):
        """Filter jobs record based on the `filter_dict` param"""
        filtered_jobs_record = {}
        filter_dict = {k: [datetime.strptime(dt, "%d-%b-%Y, %H:%M:%S IST") for dt in v]
                       if 'date' in k.lower() else v for k, v in filter_dict.items()}
        for jid, jrecord in jobs_record.items():
            filterFlag = True  # filter flag
            for fkey, frange in filter_dict.items():
                if 'date' in fkey.lower():
                    if not (min(frange) <= datetime.strptime(jrecord[fkey], "%d-%b-%Y, %H:%M:%S IST") <= max(frange)):
                        filterFlag = False
                        break
                elif all([isinstance(v, int) for v in frange]):
                    if not (min(frange) <= jrecord[fkey] <= max(frange)):
                        filterFlag = False
                        break
                elif jrecord[fkey] not in frange:
                    filterFlag = False
                    break
            if filterFlag:
                filtered_jobs_record.update({jid: jobs_record[jid]})
        return filtered_jobs_record
    
    @elapsedTime
    def arya_sourced_jobs_record(self, source_env='qa', filter_dict={}, save_path=False):
        """Derive few stats regarding the Arya sourced jobs, e.g. -- 
        - does the job exist in the retained table
        - does it exist in the toprocess and/or custom toprocess tables
        - job creation & last update dates
        """
        arya_jobs_record, job_ids = {}, sorted(list(self.job_ids), reverse=True)
        self.sourced_jobs_record = {}
        try:
            db_key = 'database' if source_env == 'qa' else f'database.{source_env}'
            db_name, jobid_key = self.db_name, self.jobid_key
            base_table, copy_table = self.base_table, self.copy_table
            toprocess_jobs = MySQLHelpers.get_all_distinct_jobs(db_key, db_name, base_table, jobid_key)
            custom_toprocess_jobs = MySQLHelpers.get_all_distinct_jobs(db_key, db_name, copy_table, jobid_key)
            retained_jobs = MySQLHelpers.transact_to_jobsretain_tbl(db_key, db_name, job_ids, 'check')
            # Get Arya job details & JTR counts
            arya_jobdetails = Parallel(n_jobs=-1)(delayed(MySQLHelpers.extract_arya_jobdetails)(db_key, jid) for jid in job_ids)
            jtr_contds = Parallel(n_jobs=-1)(delayed(MySQLHelpers.get_TopN_JTR)(db_key, jid) for jid in job_ids)
                
            # Form the sourced jobs record
            unique_jobs_record = []
            for idx, jid in enumerate(job_ids):
                if not arya_jobdetails[idx]:
                    continue
                ccompany_job_title = [arya_jobdetails[idx].get(k, '') for k in ('ClientCompany', 'JobTitle')]
                if any(ccompany_job_title) and (ccompany_job_title in unique_jobs_record):
                    continue  # Record only unique jobs w.r.t. -- ClientCompany-JobTitle
                existence_records = {
                    "is_in_toprocess": jid in toprocess_jobs,
                    "is_in_custom_toprocess": jid in custom_toprocess_jobs,
                    "is_ratined_job": jid in retained_jobs,
                    "JTRCount": len(jtr_contds[idx]),
                }
                job_record = merge_dicts((existence_records, arya_jobdetails[idx]))
                arya_jobs_record.update({jid: job_record})
                unique_jobs_record.append(ccompany_job_title)
            self.sourced_jobs_record = self._filter_jobs_record(arya_jobs_record, filter_dict)  # filter jobs record
            save_files(self.sourced_jobs_record, save_path, 'sourced_jobs_record', '.json', indent=4, default=str)
        except Exception as error:
            LOGGER.error(error)
            LOGGER.error("Unexpected Error in gathering Arya sourced jobs record !!")
            raise error


if __name__ == '__main__':
    print('python version:', sys.version)   
    print('cwd:', os.getcwd())
