import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sqs_resource = boto3.resource("sqs", region_name=AWS_REGION)
    sqs_client = boto3.client("sqs", region_name=AWS_REGION)
    
    # CONSTANTS
    QUEUE_NAME = 'hands-on-cloud-standard-s-queue'
    DLQ_NAME = 'hands-on-cloud-standard-dead-letter-queue'
    DELAY_SECONDS = '0'
    VISIBLITY_TIMEOUT = '60'
    queue = create_queue(QUEUE_NAME, DELAY_SECONDS, VISIBLITY_TIMEOUT, sqs_resource)
    print(f'Standard Queue {QUEUE_NAME} created. Queue URL - {queue.url}')
    
    dead_letter_queue = create_dead_letter_queue(DLQ_NAME, DELAY_SECONDS,VISIBLITY_TIMEOUT, sqs_resource)
    
    dlq_arn = get_queue_arn(dead_letter_queue.url, sqs_client)['Attributes']['QueueArn']
    print(f'Dead Letter Queue {DLQ_NAME} created. Queue ARN - {dlq_arn}')
    
    redrive_policy = {'deadLetterTargetArn': dlq_arn, 'maxReceiveCount': '10'}
    output = configure_queue_to_use_dlq(queue.url, redrive_policy, sqs_client)
    print(f'{QUEUE_NAME} queue is configured to use {DLQ_NAME} as dead letter queue.')
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
    
def create_queue(queue_name, delay_seconds, visiblity_timeout, sqs_resource):
    """
    Create a standard SQS queue.
    """
    try:
        response = sqs_resource.create_queue(QueueName=queue_name,
                                             Attributes={
                                                 'DelaySeconds':
                                                 delay_seconds,
                                                 'VisibilityTimeout':
                                                 visiblity_timeout
                                             })
    except ClientError:
        print(f'Could not create SQS queue - {queue_name}.')
        raise
    else:
        return response
        
def create_dead_letter_queue(dlq_name, delay_seconds, visiblity_timeout, sqs_resource):
    """
    Create a Dead letter queue.
    """
    try:
        response = sqs_resource.create_queue(QueueName=dlq_name,
                                             Attributes={
                                                 'DelaySeconds':
                                                 delay_seconds,
                                                 'VisibilityTimeout':
                                                 visiblity_timeout
                                             })
    except ClientError:
        print(f'Could not create DLQ - {dlq_name}.')
        raise
    else:
        return response

def get_queue_arn(dlq_url, sqs_client):
    """
    Returns the ARN of the Dead Letter Queue.
    """
    try:
        response = sqs_client.get_queue_attributes(QueueUrl=dlq_url,
                                                   AttributeNames=['QueueArn'])
    except ClientError:
        print(f'Could not return DLQ ARN - {dlq_url}.')
        raise
    else:
        return response

def configure_queue_to_use_dlq(queue_url, redrive_policy, sqs_client):
    """
    Configure queue to send messages to dead letter queue
    """
    try:
        response = sqs_client.set_queue_attributes(
            QueueUrl=queue_url,
            Attributes={'RedrivePolicy': json.dumps(redrive_policy)})
    except ClientError:
        print(f'Could not set RedrivePolicy on - {queue_url}.')
        raise
    else:
        return response