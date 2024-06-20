import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_client = boto3.resource("sqs", region_name=AWS_REGION)
    
    # CONSTANTS
    QUEUE_PREFIX = 'hands-on-cloud'
    lst_of_sqs_queues = filter_queues(QUEUE_PREFIX, sqs_client)
    print(f'A list of SQS queue(s) starting with prefix {QUEUE_PREFIX}:')
    for queue in lst_of_sqs_queues:
        print(f'Queue URL - {queue.url}')   
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def filter_queues(queue_prefix, sqs_client):
    """
    Creates an iterable of filtered Queue resources in the collection.
    """
    try:
        sqs_queues = []
        filtered_queues = sqs_client.queues.filter(
            QueueNamePrefix=queue_prefix)
        for queue in filtered_queues:
            sqs_queues.append(queue)
    except ClientError:
        print(f'Could not filter queues for prefix {queue_prefix}.')
        raise
    else:
        return sqs_queues