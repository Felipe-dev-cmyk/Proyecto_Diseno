from flask import Blueprint, request, jsonify
from orchestrator.TBTAFOrchestrator import TBTAFOrchestrator

executor_api = Blueprint('executor_api', __name__)

@executor_api.route('/execute', methods=['POST'])
def execute():
    data = request.get_json()

    # Validar datos entrantes
    if not data or 'test_suite_location' not in data or 'test_bed_nodes' not in data:
        return jsonify({'error': 'Missing required fields: test_suite_location or test_bed_nodes'}), 400

    test_suite_location = data['test_suite_location']
    test_bed_nodes = data['test_bed_nodes']

    # Ejecutar usando el orchestrator
    orchestrator = TBTAFOrchestrator()
    test_suite = orchestrator.createTestSuite(test_suite_location)
    execution_result = orchestrator.executeTestSuite(test_suite, test_bed_nodes)

    return jsonify({'status': 'success', 'details': execution_result.to_dict()}), 200
