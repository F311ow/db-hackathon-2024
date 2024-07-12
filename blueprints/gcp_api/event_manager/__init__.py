from flask import request, jsonify
from flask_restx import Namespace, Resource, fields
from http import HTTPStatus

event_mgr_ns = Namespace('event_manager', 'Manage event calendar')

event_model = event_mgr_ns.model('event_model',
                                 {'event_type': fields.String(description='Calendar Event Type',
                                                              required=True,
                                                              enum=['Dates', 'Bills', 'Medicine', 'Routine', 'Other']),
                                  'event_dt': fields.DateTime(description='Event datetime',
                                                              required=True),
                                  'user_id': fields.Integer(description='User Identifier',
                                                            required=True),
                                  'name': fields.String(description='Event Name',
                                                        required=True),
                                  'event_id': fields.Integer(description='Event Identifier', readonly=True)
                                  })

event_list_model = event_mgr_ns.model('event_list_model',
                                      {'events': fields.Nested(event_model,
                                                               description='List of Events',
                                                               as_list=True),
                                       'total_events': fields.Integer(description='Total number of events')})

event = {
    "event_type": "Medicine",
    "event_dt": "2024-07-12T08:00:00.000Z",
    "user_id": 123,
    "name": "Take Donepezil",
    "event_id": "1000025"
}


@event_mgr_ns.route('')
class Events(Resource):
    @event_mgr_ns.marshal_list_with(event_list_model)
    def get(self):
        event_list = [event]
        return {'events': event_list,
                'total_events': len(event_list)}

    @event_mgr_ns.marshal_list_with(event_model, code=HTTPStatus.CREATED)
    @event_mgr_ns.expect(event_model)
    def post(self):
        return event, 201


@event_mgr_ns.route('/<int:event_id>')
class Event(Resource):
    @event_mgr_ns.marshal_list_with(event_model)
    def get(self, event_id):
        return request.json

    @event_mgr_ns.marshal_list_with(event_model)
    @event_mgr_ns.expect(event_model)
    def put(self, event_id):
        return request.json

    @event_mgr_ns.response(404, 'Entity not found')
    def delete(self, event_id):
        return '', 204
