from flask import Flask,render_template,url_for,request,redirect,make_response
import sqlite3
from waitress import serve
from cloudtrail_helper import event_data 
app = Flask(__name__)


# this will be removed and  replaced with the real backend code of the project at a later date




@app.route("/profile")
def EJ_profile():
    my_name_jason = {
        "name":"Elijah Quinones",
        "about":"I am a software engineer fellow at Hack.Diversity"
    }
    return my_name_jason


@app.route("/", methods = ['GET','POST'])
def home():
    return redirect("https://itcapstone.auth.us-east-1.amazoncognito.com/login?client_id=nni18qf04rvoq1p64edejus30&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Faws1.onrender.com%2Floggedin")

@app.route("/register")
def register():
    
    return render_template("register.html")

@app.route("/loggedin")
def login():
        have_code = request.args.get('code')
        if have_code:
            return render_template("dashboard.html")
        else:
            return redirect("https://itcapstone.auth.us-east-1.amazoncognito.com/login?client_id=nni18qf04rvoq1p64edejus30&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Faws1.onrender.com%2Floggedin")


        

# Test route where AWS data is displayed. 
# Event name parameter is required 
@app.route("/test/<event_name>")
def test(event_name):
    return event_data(event_name)

@app.route("/metrics", methods = ["GET", "POST"])
def metrics():
    if  request.method == "POST":
        input = request.form['event_name']
        print(input)
        return redirect(url_for('test', event_name=input))
    else:
        return render_template("get_metrics.html")

@app.route("/boto3/cloudtrail/<event_name>/<days>")
def get_cloudtrail_data(event_name="ConsoleLogin", days=1):
    return redirect(url_for('test', event_name=event_name, days=days))

if __name__ == '__main__':
    serve(app, host='0.0.0.0', port= 50100, threads =2)
