import urllib2
from botocore.vendored import requests
import boto3
import ssl

"""
This function checks if the web page contains a given Google Analytics code. If not it triggers a SNS notification. You need to have created your SNS topic first. 
"""

websiteURL = 'https://www.clouded.ch'
findInHtml = 'UA-87368076-1'
topicArnCode = 'arn:aws:sns:eu-central-1:212124416081:website-google-analytics-code'
notificationSubject = 'Missing Google Analytics Code'
notificationMessage = 'The code UA-87368076-1 was not found on site.'

def lambda_handler(event, context):
    ssl.match_hostname = lambda cert, hostname: True
    
    response = urllib2.urlopen(websiteURL)
    page_source = response.read()

    if findInHtml in page_source: 
        print "%s found in code!" % (findInHtml)
    else:
        print "Houston we have a problem, I couldn't find %s" % (findInHtml)
        sns = boto3.client('sns')
        sns.publish(
            TopicArn = topicArnCode,
            Subject = notificationSubject,
            Message = notificationMessage
        )


