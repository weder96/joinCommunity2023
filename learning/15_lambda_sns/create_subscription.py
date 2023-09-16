import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sns_client = boto3.client("sns", region_name=AWS_REGION)
    #create_topic(topic_name, sns_client)
    
    #topics = list_topics(sns_client)
    #for topic in topics:
        #print(topic)
    
    #topic_attributes = list_topic_attributes(sns_client)
    #for topic_attribute in topic_attributes:
        #print(json.dumps(topic_attribute, indent=4, sort_keys=True))
    
    '''
    topic_arn = 'arn:aws:sns:us-east-1:710304818543:hands-on-cloud-sns-topic'
    message = 'This is a test message on topic.'
    subject = 'This is a message subject on topic.'
    print(f'Publishing message to topic - {topic_arn}...')
    message_id = publish_message(topic_arn, message, subject, sns_client)
    print(f'Message published to topic - {topic_arn} with message Id - {message_id}.')    
    '''
    
    topic_arn = 'arn:aws:sns:us-east-1:710304818543:hands-on-cloud-sns-topic'
    print(f'Deleting a SNS topic...')
    delete_response = delete_topic(topic_arn, sns_client)
    print(f'Deleted a topic - {topic_arn} successfully.')
    
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
        
def create_subscription(name, sns_client):
    print(f'Created subscription')

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
        

def delete_topic(topic_arn, sns_client):
    """
    Delete a SNS topic.
    """
    try:
        response = sns_client.delete_topic(TopicArn=topic_arn)
    except ClientError:
        logger.exception(f'Could not delete a SNS topic.')
        raise
    else:
        return response
    