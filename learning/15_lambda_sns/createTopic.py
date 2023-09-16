import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sns_client = boto3.client("sns", region_name=AWS_REGION)
    create_topic(topic_name, sns_client)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SNS Topic from Lambda!!!')
    }

def create_topic(name, sns_client):
    """
    Creates a SNS notification topic.
    """
    topic_name = 'hands-on-cloud-sns-topic'
    print(f'Creating SNS topic {topic_name}...')
    try:
        topic = sns_client.create_topic(Name=name)
        print(f'Created SNS topic {name}.')
    except ClientError:
        print(f'Could not create SNS topic {name}.')
        raise
    else:
        return topic