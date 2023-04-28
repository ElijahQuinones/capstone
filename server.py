from flask import Flask,render_template,request,redirect
from waitress import serve
from cloudtrail_helper import event_data, displayAll
app = Flask(__name__)



@app.route("/", methods = ['GET','POST'])
def home():
    return redirect("https://itcapstone.auth.us-east-1.amazoncognito.com/login?client_id=nni18qf04rvoq1p64edejus30&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Faws1.onrender.com%2Floggedin")

@app.route("/loggedin", methods = ['GET','POST'])
def login():
        have_code = request.args.get('code')
        if have_code:
            return render_template("dashboard.html")
        else:
            return redirect("https://itcapstone.auth.us-east-1.amazoncognito.com/login?client_id=nni18qf04rvoq1p64edejus30&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Faws1.onrender.com%2Floggedin")



# get_data is for testing purposes 
# Event name parameter is required 
@app.route("/getData/<event_name>/<int:days>")
def get_data(event_name, days):
    return event_data(event_name, days)

@app.route("/boto3/cloudtrail/<event_name>/<int:days>")
def get_cloudtrail_data(event_name, days):
    # limit days to 90 
    # Try Catch statement
    # print("The event name is " + event_name)
    # print("The days variable contains " + str(days))
    return event_data(event_name, days)

    # return redirect(url_for('get_data', event_name=event_name, days=days))
@app.route("/alldata")
def displayData():
     return displayAll()
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port= 50100, threads =2)
    
    
