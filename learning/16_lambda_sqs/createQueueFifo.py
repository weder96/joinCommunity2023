import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_client = boto3.resource("sqs", region_name=AWS_REGION)
    
    QUEUE_NAME = 'hands-on-cloud-fifo-queue-a.fifo'
    DELAY_SECONDS = '0'
    VISIBLITY_TIMEOUT = '60'
    output = create_queue_fifo(QUEUE_NAME, DELAY_SECONDS, VISIBLITY_TIMEOUT, sqs_client)
    print(f"Standard Queue {QUEUE_NAME}  created. Queue URL {output}")
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        
def create_queue_fifo(queue_name, delay_seconds, visiblity_timeout, sqs_client):
    """
    Create a First In First Out (FIFO) SQS queue
    """
    try:
        response = sqs_client.create_queue(QueueName=queue_name,
                                             Attributes={
                                                 'DelaySeconds': delay_seconds,
                                                 'VisibilityTimeout': visiblity_timeout,
                                                 'FifoQueue': 'true'
                                             })
    except ClientError:
        print("Could not create SQS queue"+ queue_name)
        raise
    else:
        return response

