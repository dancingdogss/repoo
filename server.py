from flask import Flask as fl
from flask import render_template
from app import *
server = fl(__name__)

@server.route("/", methods=["GET","POST"])
def session1():
    return render_template("session1.html")

if __name__=="__main__":
    server.run(debug=True)

