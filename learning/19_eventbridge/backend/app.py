import json
from datetime import datetime
import boto3

# EventBridge client
eventbridge_client = boto3.client('events')


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)

    response = {
        'statusCode': 200,
        'body': json.dumps('successfully created item!'),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    
    return response