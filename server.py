from flask import Flask,render_template,url_for

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
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

if __name__ == '__main__':
    app.run(debug=True)