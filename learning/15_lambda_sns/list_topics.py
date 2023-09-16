import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sns_client = boto3.client("sns", region_name=AWS_REGION)    
    
    topics = list_topics(sns_client)
    for topic in topics:
        print(topic)
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SNS Topic from Lambda!!!')
    }

def list_topics(sns_client):
    """
    Lists all SNS notification topics using paginator.
    """
    print(f'List Topic')
    try:
        paginator = sns_client.get_paginator('list_topics')
        # creating a PageIterator from the paginator
        page_iterator = paginator.paginate().build_full_result()
        topics_list = []
        # loop through each page from page_iterator
        for page in page_iterator['Topics']:
            topics_list.append(page['TopicArn'])
    except ClientError:
        print(f'Could not list SNS topics.')
        raise
    else:
        return topics_list