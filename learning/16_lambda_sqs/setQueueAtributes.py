import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_client = boto3.client("sqs", region_name=AWS_REGION)
    
    # Constants
    QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/710304818543/hands-on-cloud-standard-queue'
    DELAY_SECONDS = '15'
    MAX_MSG_SIZE = '2048'
    queue = configure_queue_attributes(QUEUE_URL, DELAY_SECONDS, MAX_MSG_SIZE, sqs_client)
    print(f'Queue {QUEUE_URL} attributes created.')
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def configure_queue_attributes(queue_url, delay_seconds, max_msg_size, sqs_client):
    """
    Configure queue attributes.
    """
    try:
        response = sqs_client.set_queue_attributes(QueueUrl=queue_url,
                                                   Attributes={
                                                       'DelaySeconds':
                                                       delay_seconds,
                                                       'MaximumMessageSize':
                                                       max_msg_size
                                                   })
    except ClientError:
        print(f'Could not set attributes on - {queue_url}.')
        raise
    else:
        return response