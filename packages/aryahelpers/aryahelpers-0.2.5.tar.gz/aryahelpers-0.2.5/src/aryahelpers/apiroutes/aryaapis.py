"""Flask apis to perform automated Arya job and candidates operations"""

import logging
from appconfig import COPY_JOB_LIMIT
from utils.genericutils import null_handler
from joboperations.jobs import AryaJobOperations
from joboperations.contenders import AryaSourcedContenders
from flask import Blueprint, request, abort, jsonify

LOGGER = logging.getLogger(__name__)

bp = Blueprint('aryajobs', __name__)


@bp.route('/copy_jobs', methods=['POST'])
def copy_jobs():
    """The copy job route. Example URL, request payload and output are shown below.
    URL = http://192.168.38.99:1511/copy_jobs\n
    payload = {
        "job_ids": [388762, 388763],
        "source_and_target_envs": ["qa", "staging"],
        "source_and_target_users": ["dsqatesting@leoforce.com", "sreevally.pasumarthy@leoforce.com"],
        "target_jobs_status": 1,
        "to_retain_job": false
    }\n
    response = [
        { "source_job": 388762, "target_job": 202470 },
        { "source_job": 388763, "target_job": 202475 }
    ]
    """
    payload = request.json
    joboperations_obj = AryaJobOperations()
    validationFlag = joboperations_obj.validate_copy_jobs_payload(payload)
    if not validationFlag:
        invalid_reqstr = f"Invalid request !! Job ids, source and target environments, source and target emails are \
            required to process the request. Also, total job ids should not exceed {COPY_JOB_LIMIT}."
        abort(400, invalid_reqstr)
    joboperations_obj.copy_jobs_from_source_to_target(payload, True)
    return jsonify(joboperations_obj.copyjobs_info)


@bp.route('/<source_env>/jobs_record', methods=['POST'])
def jobs_record(source_env='qa'):
    """The Arya sourced jobs route. Example URL and request payload are shown below.\n
    URL = http://192.168.38.99:1511/qa/jobs_record\n
    payload = {
        "job_ids": [387814, 387815, 387816, 387817],
        "filter_dict": {
            "JobCreatedEmail": ["sreevally.pasumarthy@leoforce.com", "dsqatesting@leoforce.com" ],
            "JobCreatedDate" : ["01-Nov-2023, 00:00:00 IST", "07-Dec-2023, 00:00:00 IST"]
        },
        "save_path": "/path_to_save"
    }
    """
    try:
        response = {}
        payload = request.json
        job_ids = payload.get("job_ids", [])
        filter_dict = payload.get("filter_dict", {})
        save_path = payload.get("save_path", False)
        joboperations_obj = AryaJobOperations(job_ids=job_ids)
        joboperations_obj.arya_sourced_jobs_record(source_env, filter_dict, save_path)
        response = joboperations_obj.sourced_jobs_record
    except Exception as error:
        LOGGER.error('Failed in copying jobs from source to target user !')
        LOGGER.exception(error)
    return jsonify(response)


@bp.route('/<source_env>/access_aryacontds', methods=['POST'])
def access_aryacontds(source_env='qa'):
    """The route for accessing Arya sourced contenders. The example URL, payload and output is shown below.\n
    URLs
        http://192.168.38.99:1511/qa/access_aryacontds?show=summary&top=20
        http://192.168.38.99:1501/prod/access_aryacontds?show=summary&sort=false&top=20\n
    payload = {
        "job_ids": [387019, 111111, 387018],
        "save_type": ".json",
        "save_path": "/path_to_save"
    }\n
    response = {
        "387019": "Accessed candidates: 20",
        "111111": "Accessed candidates: 0",
        "387018": "Accessed candidates: 20",
    }
    """
    try:
        response = {}
        payload = request.json
        top_contds = int(null_handler(request.args.get('top'), '300'))
        to_sort = True if request.args.get('sort', 'false').lower() == 'true' else False  # to sort job ids
        req_response = request.args.get('show', 'all')  # show = ['all', 'summary']
        job_ids = payload.get("job_ids", [])
        save_path = payload.get("save_path", False)
        save_type = payload.get("save_type", '.json')
        sourcedcontds_obj = AryaSourcedContenders(
            source_env=source_env, job_ids=job_ids, top_contds=top_contds, to_sort=to_sort)
        sourcedcontds_obj.access_contdsinfo(save_path, save_type)
        response = sourcedcontds_obj.arya_sourcedcontds if req_response == 'all' else sourcedcontds_obj.contds_count
    except Exception as error:
        LOGGER.error('Failed to access Arya sourced contenders for the given job ids !')
        LOGGER.exception(error)
    return jsonify(response)


@bp.route('/group_aryacontds', methods=['POST'])
def group_aryacontds():
    """The route for grouping info of same contenders, sourced into nultiple jobs.\n
    URL = http://192.168.38.99:1511/group_aryacontds?show=summary&top=20\n
    payload = {
        "jobs_info": [
            {"qa": 388775, "staging": 202504},
            {"qa": 388774, "staging": 202496},
            {"qa": 388778, "staging": 202528}
        ],
        "save_type": ".json",
        "save_path": "/path_to_save"
    }\n
    response = {
        "group-0": "5 same contenders sourced for these jobs",
        "group-1": "8 same contenders sourced for these jobs",
        "group-2": "3 same contenders sourced for these jobs"
    }
    """
    try:
        response = {}
        payload = request.json
        top_contds = int(null_handler(request.args.get('top'), '300'))
        req_response = request.args.get('show', 'all')  # show = ['all', 'summary']
        jobs_info = payload.get("jobs_info", [])
        save_path = payload.get("save_path", False)
        save_type = payload.get("save_type", '.json')
        groupcontds_obj = AryaSourcedContenders(jobs_info=jobs_info, top_contds=top_contds)
        groupcontds_obj.group_samecontdsinfo(save_path, save_type)
        response = groupcontds_obj.arya_groupcontds if req_response == 'all' else groupcontds_obj.groupcontds_count
    except Exception as error:
        LOGGER.error('Failed to group Arya sourced contenders for the given jobs !')
        LOGGER.exception(error)
    return jsonify(response)
