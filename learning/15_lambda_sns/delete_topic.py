import json
import boto3
from botocore.exceptions import ClientError


def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    AWS_REGION = "us-east-1"
    sns_client = boto3.client("sns", region_name=AWS_REGION)
    
    topic_arn = 'arn:aws:sns:us-east-1:710304818543:hands-on-cloud-sns-topic'
    print(f'Deleting a SNS topic...')
    delete_response = delete_topic(topic_arn, sns_client)
    print(f'Deleted a topic - {topic_arn} successfully.')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World Client SNS Topic from Lambda!!!' + str(delete_response))
    }    

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
    