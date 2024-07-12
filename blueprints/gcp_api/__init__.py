from flask import Blueprint
from flask_restx import Api
from blueprints.gcp_api.ai_tools import vertex_ns
from blueprints.gcp_api.event_manager import event_mgr_ns

gcp_api_bp = Blueprint('gcp_api', __name__, url_prefix='/gcp-api')

api_extension = Api(gcp_api_bp, title='Test API', version='1.0', description='Test API Description', doc='/doc')
api_extension.add_namespace(vertex_ns)
api_extension.add_namespace(event_mgr_ns)
