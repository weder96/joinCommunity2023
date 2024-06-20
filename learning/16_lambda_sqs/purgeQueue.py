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
    purge = purge_queue(QUEUE_URL, sqs_client)
    print(f'All the message from {QUEUE_URL} are purged.')
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def purge_queue(queue_url, sqs_client):
    """
    Deletes the messages in a specified queue
    Deleting all the messages from the queue can take up to 60 seconds.
    """
    try:
        response = sqs_client.purge_queue(QueueUrl=queue_url)
    except ClientError:
        print(f'Could not purge the queue - {queue_url}.')
        raise
    else:
        return response