"""Flask api to access candidates explanations from DB"""
# http://192.168.38.99:1501/explanations/qa?expl_type=facts&job_id=359229&name=Vinay%20Pratap
# http://192.168.38.99:1501/explanations/qa?expl_type=facts&job_id=371151&recommendation_status_id=3
# http://192.168.38.99:1501/explanations/qa?expl_type=company&job_id=359228&num_candidates=10
# http://192.168.38.99:1501/explanations/staging?job_id=199436&num_candidates=20
# http://192.168.38.99:1501/explanations/prod?job_id=2837022&num_candidates=20

import logging
from aryatestbed.explaccess import AccessExplanations
from flask import Blueprint, request, jsonify

LOGGER = logging.getLogger(__name__)

bp = Blueprint('explanations', __name__)


@bp.route('/explanations/<base_env>', methods=['GET'], strict_slashes=False)
def expl_func(base_env=None):
    try:
        response = []
        # Access input params
        job_id = request.args.get('job_id')
        num_candidates = request.args.get('num_candidates')
        if num_candidates:
            num_candidates = int(num_candidates)
        candidate_name = request.args.get('name')
        candidate_guid = request.args.get('guid')
        recommendation_status_id = request.args.get('recommendation_status_id')
        explanation_type = request.args.get('expl_type', 'facts').lower()
        if recommendation_status_id:
            recommendation_status_id = int(recommendation_status_id)
        accessor = AccessExplanations(
            job_id=job_id, num_candidates=num_candidates, candidate_name=candidate_name,
            candidate_guid=candidate_guid, recommendation_status_id=recommendation_status_id,
            explanation_type=explanation_type, base_env=base_env)
        response = accessor.access_explanations()
    except Exception as error:
        LOGGER.error('Failed in accessing candidates explanations from DB !')
        LOGGER.exception(error)
    return jsonify(response)
