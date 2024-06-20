import json
import boto3
from boto3 import dynamodb
from boto3.dynamodb.conditions import Key, Attr


def lambda_handler(event, context):
    print('Starting input lambda function call')
    print(event)

    print(event['pathParameters']['id'])

    idParam = event['pathParameters']['id']

    client = boto3.client('dynamodb')
    item = client.delete_item( TableName='orders' ,Key={'orderId': { 'S' : str(idParam)}})

    print("The query returned the following item:")
    print(item)

    response = {
        'statusCode': 200,
        'body': 'Item delete with Successfully :'+ str(json.dumps(item)),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return response