from botocore.vendored import requests
import boto3
 
"""
This function checks is a given website is alive. If not it triggers a SNS notification. You need to have created your SNS topic first. 
"""

websiteURL = 'https://www.clouded.ch'
topicArnCode = 'arn:aws:sns:eu-central-1:212124416081:website-offline'

def lambda_handler(event, context):
    r = requests.head(websiteURL) 
    if r.status_code == 200:
        print "Website Is Alive!"
    else:
        sns = boto3.client('sns')
        sns.publish(
            TopicArn = topicArnCode,
            Subject = 'Website Offline' ,
            Message = 'Status code 200 was expected but returned was '+ str(r.status_code)
        )

