from flask import Flask, jsonify, request
from err_msg import *

from models.user import User
from models.key import Key

app = Flask(__name__)


@app.route("/register", methods=["POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        firstName = request.form["firstname"]
        lastName = request.form["lastname"]

        obj_user = User()
        isCreated = not (obj_user.create(username, password, firstName, lastName))
        obj_user.close()
        if isCreated:
            return jsonify({"message": ""}), 200
        else:
            return jsonify({"message": ERR_REQUEST_MSG}), 400


@app.route("/update-user-info", methods=["POST"])
def updateUserInfo():
    if request.method == "POST":
        userID = request.form["id"]
        firstName = request.form["firstname"]
        lastName = request.form["lastname"]

        obj_user = User()
        isUpdated = not (obj_user.updateInfo(userID, firstName, lastName))
        obj_user.close()
        if isUpdated:
            return jsonify({"message": ""}), 200
        else:
            return jsonify({"message": ERR_REQUEST_MSG}), 400


@app.route("/generate-api-key", methods=["GET"])
def generateApiKey():
    if request.method == "GET":
        obj_key = Key()
        key = (obj_key.generateKey(1))["key"]
        hasKey = not (key)
        obj_key.close()
        if hasKey:
            return jsonify({"key": key}), 200
        else:
            return jsonify({"key": None}), 400


@app.route("/verify-api-key", methods=["POST"])
def verifyApiKey():
    if request.method == "POST":
        apiKey = request.form["token"]
        obj_key = Key()
        isValid = obj_key.verifyKey(apiKey)
        obj_key.close()
        if isValid:
            return jsonify({"msg": ""}), 200
        else:
            return jsonify({"msg": "Invalid key"}), 400


@app.route("/get-user-details/<int:userid>/<string:token>/", methods=["GET"])
def getUserDetails(userid, token):
    if request.method == "GET":
        obj_user = User()
        res = obj_user.fetch(userid)
        isEmptyResult = res["username"] == ""
        if not isEmptyResult:
            obj_user.close()
            return jsonify(res), 200
        else:
            return jsonify({"msg": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)
