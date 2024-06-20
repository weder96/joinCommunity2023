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
    MSG_ATTRIBUTES = {
        'Title': {
            'DataType': 'String',
            'StringValue': 'Working with SQS in Python using Boto3'
        },
        'Author': {
            'DataType': 'String',
            'StringValue': 'Abhinav D'
        }
    }
    MSG_BODY = 'Learn how to create, receive, delete and modify SQS queues and see the other functions available within the AWS.'
    msg = send_queue_message(QUEUE_URL, MSG_ATTRIBUTES, MSG_BODY, sqs_client)
    json_msg = json.dumps(msg, indent=4)
    print(f'''
        Message sent to the queue {QUEUE_URL}.
        Message attributes: \n{json_msg}'''
        )
    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SQS Queue from Lambda!!!')
    }
        

def send_queue_message(queue_url, msg_attributes, msg_body, sqs_client):
    """
    Sends a message to the specified queue.
    """
    try:
        response = sqs_client.send_message(QueueUrl=queue_url,
                                           MessageAttributes=msg_attributes,
                                           MessageBody=msg_body)
    except ClientError:
        print(f'Could not send meessage to the - {queue_url}.')
        raise
    else:
        return response