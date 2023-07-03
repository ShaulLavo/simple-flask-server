from flask import Blueprint, render_template, request, jsonify

print(__name__)

views = Blueprint(__name__, "views")



@views.route("/")
def home():
    return render_template("index.html", name="Joe")


@views.route('/profile')
def profile(username):
    args = request.args
    print('args:', args)
    name = args.get('name')
    return render_template("index.html", name=name)



@views.route("/json")
def get_json():
    return jsonify({"name": "Joe", "age": 30})



@views.route("/data")
def get_data():
    data =request.json
    print('data:', data)
    return jsonify(data)