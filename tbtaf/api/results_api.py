from flask import Blueprint, request, jsonify
from orchestrator.TBTAFOrchestrator import TBTAFOrchestrator

results_api = Blueprint('results_api', __name__)
orchestrator = TBTAFOrchestrator()

@results_api.route('/api/suite_results', methods=['GET'])
def suite_results():
    suite_id = request.args.get('suite_id')

    if not suite_id:
        return jsonify({"status": "error", "message": "suite_id is required"}), 400

    try:
        results = orchestrator.getResultReport(suite_id)
        return jsonify({"status": "success", "results": results}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
