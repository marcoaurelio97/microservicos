#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from enviar_email import send_email
from reservar_quadra import verify_availability


app = Flask(__name__)
api = Api(app)


class SendEmail(Resource):
    def post(self):
        email = request.json['email']
        text = request.json['text']

        send_email(email, text)

        return jsonify({'status': True})


class VerifyAvailability(Resource):
    def post(self):
        grupo = request.json['grupo']
        quadra = request.json['quadra']
        dataInicio = request.json['dataInicio']
        dataFim = request.json['dataFim']

        status = verify_availability(grupo, quadra, dataInicio, dataFim)

        return jsonify({'status': status})


api.add_resource(SendEmail, '/email')
api.add_resource(VerifyAvailability, '/reserve')

if __name__ == '__main__':
    app.run(port=5002)
