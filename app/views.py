from flask import Flask, request, jsonify,Blueprint
from flask_restful import Api, Resource

main = Blueprint('main', __name__)

@main.route('/TinhThanhPho', methods=["GET"])
def ListTinhThanhPho():
    pass


