import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_client = boto3.resource("sqs", region_name=AWS_REGION)
    
    lst_of_sqs_queues = list_queues(sqs_client)
    for queue in lst_of_sqs_queues:
        print(f"Queue URL - {queue}")    
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def list_queues(sqs_client):
    """
    Creates an iterable of all Queue resources in the collection.
    """
    try:
        sqs_queues = []
        for queue in sqs_client.queues.all():
            sqs_queues.append(queue)
    except ClientError:
        print('Could not list queues.')
        raise
    else:
        return sqs_queues