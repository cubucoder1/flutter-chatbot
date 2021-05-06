from flask import flask, jsonify, request
import time 
app = flask(_name_)
@app.route("/bot" , method = ["POST"])


def response() :
    query = dict(request.form)['query']

    result = query + " " + time.ctime()
    return jsonify({"response" : result})


if _name_ == "_main_":
    app.run(host = "0.0.0.0" , )