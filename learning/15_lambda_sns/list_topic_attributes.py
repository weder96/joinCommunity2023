import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sns_client = boto3.client("sns", region_name=AWS_REGION)    
    
    topic_attributes = list_topic_attributes(sns_client)
    for topic_attribute in topic_attributes:
        print(json.dumps(topic_attribute, indent=4, sort_keys=True))
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SNS Topic from Lambda!!!')
    }

        
def list_topic_attributes(sns_client):
    """
    Lists all SNS topics attributes using paginator.
    """
    try:
        paginator = sns_client.get_paginator('list_topics')
        # creating a PageIterator from the paginator
        page_iterator = paginator.paginate().build_full_result()
        topic_attributes_list = []
        # loop through each page from page_iterator
        for page in page_iterator['Topics']:
            response = sns_client.get_topic_attributes(TopicArn=page['TopicArn'])['Attributes']
            dict_obj = {
                'TopicArn': page['TopicArn'],
                'TopicPolicy': json.loads(response['Policy'])
            }
            topic_attributes_list.append(dict_obj)
            
    except ClientError:
        print(f'Could not get SNS topic attributes.')
        raise
    else:
        return topic_attributes_list