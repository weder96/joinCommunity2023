import json
import boto3
from boto3.dynamodb.conditions import Key, Attr

client = boto3.resource('dynamodb')

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)

    table = client.Table('orders')
    #responseScan = table.scan(FilterExpression=Attr('Name').eq('Weder Sousa'))
    responseScan = table.scan()

    print("The query returned the following items:")
    for item in responseScan['Items']:
        print(item)    
    
    response = {
        'statusCode': 200,
        'body': json.dumps(responseScan['Items']),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    
    return response