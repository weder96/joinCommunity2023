import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_client = boto3.resource("sqs", region_name=AWS_REGION)
    
    # CONSTANTS
    QUEUE_NAME = 'hands-on-cloud-standard-queue'
    queue = get_queue(QUEUE_NAME, sqs_client)
    print(f'Queue URL - {queue}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def get_queue(queue_name, sqs_client):
    """
    Returns the URL of an existing Amazon SQS queue.
    """
    try:
        response = sqs_client.get_queue_by_name(QueueName=queue_name)
        return response
    except ClientError:
        print(f'Could not get the {queue_name} queue.')
        raise
    else:
        return response