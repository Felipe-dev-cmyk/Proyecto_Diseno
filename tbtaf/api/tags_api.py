from flask import Blueprint, request, jsonify
from orchestrator.TBTAFOrchestrator import TBTAFOrchestrator

tags_api = Blueprint('tags_api', __name__)
orchestrator = TBTAFOrchestrator()

@tags_api.route('/api/tests_by_tag', methods=['GET'])
def tests_by_tag():
    project_name = request.args.get('project_name')
    tag = request.args.get('tag')

    if not project_name or not tag:
        return jsonify({"status": "error", "message": "project_name and tag are required"}), 400

    try:
        tests = orchestrator.getTests(project_name, [tag])
        return jsonify({"status": "success", "tests": tests}), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500
