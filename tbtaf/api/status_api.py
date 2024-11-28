from flask import Blueprint, request, jsonify
from orchestrator.TBTAFOrchestrator import TBTAFOrchestrator

status_api = Blueprint('status_api', __name__)
orchestrator = TBTAFOrchestrator()

@status_api.route('/api/suite_status', methods=['GET'])
def suite_status():
    suite_id = request.args.get('suite_id')

    if not suite_id:
        return jsonify({"status": "error", "message": "suite_id is required"}), 400

    try:
        status = orchestrator.getStatus(suite_id)
        return jsonify({
            "status": "success",
            "suite_status": status.getExecutionStatusType(),
            "completion_percentage": status.getCompletionPercentage()
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
