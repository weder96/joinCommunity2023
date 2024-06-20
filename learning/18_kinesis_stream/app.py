import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)

    data = client.put_item(
    TableName='your-table-name',
    Item={
        {'id': {'S': '1'}, 'status': {'S': 'IN_PROGRESS'}, 'desc': {'S': 'Xiomi readmi 11 order'}, 'orderDate': {'S': '2023-08-10'}}
    }
    )

    print(data)
    response = {
        'statusCode': 200,
        'body': json.dumps('successfully created item!'),
        'headers': {
            'Content-Type': 'application/json',
            'Access-Control-Allow-Origin': '*'
        },
    }
    
    return response