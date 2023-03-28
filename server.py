from flask import Flask,render_template,url_for,request,redirect
import sqlite3
from waitress import serve
import boto3
import os
import json
import datetime
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
def login():
    return redirect("https://it114capstone.auth.us-east-1.amazoncognito.com/login?client_id=nni18qf04rvoq1p64edejus30&response_type=code&scope=email+openid+phone&redirect_uri=https%3A%2F%2Faws1.onrender.com%2Floggedin")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/loggedin")
def login():
    return render_template("dashboard.html")

# Test route where AWS data is displayed. 
# Event name parameter is required 
@app.route("/test/<event_name>")
def test(event_name):
    id = os.environ.get('AWS_ACCESS_KEY_ID')
    key = os.environ.get('AWS_ACCESS_KEY_KEY')

    cloudtrail = boto3.client(
        'cloudtrail',
        aws_access_key_id=id,
        aws_secret_access_key=key,
    )

    # response = cloudtrail.list_trails(
    #     NextToken='string'
    # )
    # response = cloudtrail.start_query(
    #     QueryStatement='SELECT * FROM my-0701-cloudtrail*',
    #     # DeliveryS3Uri='string'
    # )

    response = cloudtrail.lookup_events(
        LookupAttributes=[
            {
                'AttributeKey': 'EventName',
                'AttributeValue': event_name
            },
        ],
        # StartTime=datetime.datetime(2022, 12, 1),
        # EndTime=datetime.datetime(2023, 2, 28),
        # EventCategory='insight',
        MaxResults=2,
        # NextToken='50'
    )
    
    print('Existing trails:')
    return response
    # for bucket in response['Buckets']:
    #     return (f'  {bucket["Name"]}')

@app.route("/metrics", methods = ["GET", "POST"])
def metrics():
    if  request.method == "POST":
        input = request.form['event_name']
        print(input)
        return redirect(url_for('test', event_name=input))
    else:
        return render_template("get_metrics.html")


if __name__ == '__main__':
    serve(app, host='0.0.0.0', port= 50100, threads =2)
