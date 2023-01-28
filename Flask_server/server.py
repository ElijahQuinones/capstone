from flask import Flask

app = Flask(__name__)

# this will be removed and  replaced with the real backend code of the project at a later date

@app.route("/profile")
def EJ_profile():
    my_name_jason = {
        "name":"Elijah Quinones",
        "about":"I am a software engineer fellow at Hack.Diversity"
    }
    return my_name_jason

@app.route("/")
def welcome():
    return "Welcome to our capstone project"

