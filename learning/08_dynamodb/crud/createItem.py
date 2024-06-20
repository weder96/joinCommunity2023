import json
import boto3
import uuid

client = boto3.resource('dynamodb')

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event['body'])
    table = client.Table('orders')
    myuuid = uuid.uuid4()
    
    print('Your UUID is: ' + str(myuuid))
    
    order=json.loads(event['body'])
    
    data = table.put_item(
            Item={ 
                'orderId':  str(myuuid),
                'orderDate': order['orderDate'],
                'status': order['status'], 
                'desc': order['desc'], 
                'updateOrderDate': order['updateOrderDate'],
                'Name': order['Name'],
                'Email': order['Email']
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