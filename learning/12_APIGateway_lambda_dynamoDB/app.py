import json
import boto3

client = boto3.client('dynamodb')

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    route = event["routeKey"]
    
    match route: #Python 3.10
        case "GET /product":
            message = 'successfully List All itens!'
            _get_all_product()
            return _response_function(message)
        
        case "GET /product/{id}":
            id = event["pathParameters"]["id"]
            message = "Processing Get Products by id: "+ id
            _get_product_by_id(id)
            return _response_function(message)
            
        case "POST /product":
            body = event["body"]
            message = "Processing Post Product Id with "+ body
            _save_product(body)
            return _response_function(message)
            
        case "PUT /product/{id}":
            body = event["body"]
            message = "Processing PUT Product Id with "+ body
            _update_product(body)
            return _response_function(message)
        
        case "DELETE /product/{id}":
            id = event["pathParameters"]["id"]
            message = "Processing DELETE Product Id with "+ id
            _delete_product(id)
            return _response_function(message)
        
def _get_all_product():
    print("Processing Get All Products")
    
def _get_product_by_id(id):
    print(id)
    
def _delete_product(id):
    print(id)
    
def _update_product(body):
    print(body)
    
def _save_product(body):
    print(body)
    data = client.put_item(
    TableName='Order',
        Item={
            'id': {'S': '9'}, 
            'status': {'S': 'IN_PROGRESS'}, 
            'desc': {'S': 'Xiomi Redmi 13'}, 
            'orderDate': {'S': '2023-08-16'}
        }
    )

    print(data)
    
def _response_function(message):
    response = {
        'statusCode': 200,
        'body': json.dumps(message),
        'headers': {'Content-Type': 'application/json','Access-Control-Allow-Origin': '*'},
    }
            
    return response