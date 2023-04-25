import boto3
import os
from dotenv import load_dotenv
import json
import datetime
load_dotenv(".env")


# Event date takes an event name and an interger 1-90. The day argument 
# determines the date range to be logged.

def event_data(event_name, days):
  id = os.getenv("MY_ID")
  key = os.getenv("MY_ID_PASS")

  today = datetime.date.today()
  newdate = today - datetime.timedelta(days)

  cloudtrail = boto3.client(
    'cloudtrail',
    aws_access_key_id=id,
    aws_secret_access_key=key,
    region_name='us-east-2',
  )

  response = cloudtrail.lookup_events(
    LookupAttributes=[
      {
        'AttributeKey': 'EventName',
        'AttributeValue': event_name
      },
    ],

    StartTime=datetime.datetime(newdate.year, newdate.month, newdate.day),
    # EndTime=datetime.datetime(2023, 4, 7),
    # StartTime=datetime.datetime(newdate.year, newdate.month, newdate.day),
    # EndTime=datetime.datetime(today.year, today.month, today.day),
    # EventCategory='insight',
    MaxResults=1000,
    # NextToken='50'
  )

  return response
  # for bucket in response['Buckets']:
  #     return (f'  {bucket["Name"]}')
