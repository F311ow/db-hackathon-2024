import os
from flask import Flask
from flask_cors import CORS
from blueprints.gcp_api import gcp_api_bp

app = Flask(__name__)
CORS(app)

app.config['RESTPLUS_MASK_SWAGGER'] = False

with app.app_context():
    app.register_blueprint(gcp_api_bp)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
