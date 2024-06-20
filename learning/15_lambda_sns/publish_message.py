import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sns_client = boto3.client("sns", region_name=AWS_REGION)
 
    topic_arn = 'arn:aws:sns:us-east-1:710304818543:hands-on-cloud-sns-topic'
    message = 'This is a test message on topic.'
    subject = 'This is a message subject on topic.'
    print(f'Publishing message to topic - {topic_arn}...')
    message_id = publish_message(topic_arn, message, subject, sns_client)
    print(f'Message published to topic - {topic_arn} with message Id - {message_id}.')    
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SNS Topic from Lambda!!!')
    }  

def publish_message(topic_arn, message, subject, sns_client):
    """
    Publishes a message to a topic.
    """
    try:
        response = sns_client.publish(
            TopicArn=topic_arn,
            Message=message,
            Subject=subject,
        )['MessageId']
    except ClientError:
        print(f'Could not publish message to the topic.')
        raise
    else:
        return response