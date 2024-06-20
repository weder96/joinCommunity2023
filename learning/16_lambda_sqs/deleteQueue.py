import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_client = boto3.client("sqs", region_name=AWS_REGION)
    
    # Constants
    QUEUE_URL = 'https://sqs.us-east-1.amazonaws.com/710304818543/MyProjectStack-MyProjectQueueA52AEA8E-xnr5GKDvNVJG'
    queue = delete_queue(QUEUE_URL, sqs_client)
    print(f'{QUEUE_URL} deleted successfully.')   
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def delete_queue(queue_name, sqs_client):
    """
    Deletes the queue specified by the QueueUrl.
    """
    try:
        response = sqs_client.delete_queue(QueueUrl=queue_name)
    except ClientError:
        logger.exception(f'Could not delete the {queue_name} queue.')
        raise
    else:
        return response