import json
import boto3
from boto3.dynamodb.conditions import Key



def lambda_handler(event, context):
    print('Starting input lambda function call')
    print(event)


    client = boto3.client('dynamodb')

    print(event['pathParameters']['id'])
    idParam = event['pathParameters']['id']

    order=json.loads(event['body'])

    # put (idempotent)
    data = client.update_item(
        TableName="orders",
        Key={
            "orderId": {"S": str(idParam)},
        },
        ExpressionAttributeValues={
            ":val1":  {"S": order['status']},
            ":val2":  {"S": order['updateOrderDate']},
        },
        ExpressionAttributeNames={
            "#updateOrderDate": "updateOrderDate",
            "#status":"status"
        },
        UpdateExpression="set #status = :val1, #updateOrderDate = :val2 ",
        ReturnValues="ALL_NEW"
    )

    print(data)

    responseJson = {
        'statusCode': 200,
        'body': json.dumps('successfully Update item!'),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }

    return responseJson