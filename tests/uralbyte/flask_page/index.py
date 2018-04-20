from flask_oauth import OAuth
from flask import Flask, request
app =

@app.route("/")
def hello():
    return "Hello World!"


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return 'POST'
    else:
        # data = dir(request)
        return request.form
