from flask import request, jsonify
from flask_restx import Namespace, Resource, reqparse
from google.cloud import language_v2

vertex_ns = Namespace('ai_tools', 'Vertex AI interface')

classify_parser = reqparse.RequestParser()
classify_parser.add_argument('input_text', required=True, type=str, help='Text to classify')


@vertex_ns.route('/classify')
class ClassLang(Resource):
    @vertex_ns.expect(classify_parser)

    def get(self):
        input_text = request.args.get('input_text')
        res_list = []
        for cat in classify_text_v2(input_text):
            res_list.append({'category': cat.name, 'confidence': cat.confidence})
        return jsonify(res_list)


def classify_text_v2(text_content):
    """
    Classifying Content in a String

    Args:
      text_content The text content to analyze.
    """

    nlp_client = language_v2.LanguageServiceClient()

    # Initialize request argument(s)
    document = language_v2.Document()
    document.content = text_content
    document.type_ = language_v2.Document.Type.PLAIN_TEXT

    nlp_request = language_v2.ClassifyTextRequest(document=document)

    # Make the request
    response = nlp_client.classify_text(request=nlp_request)

    # Handle the response
    return response.categories
