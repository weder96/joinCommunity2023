import json
import boto3


def lambda_handler(event, context):  
    print('Received event:',json.dumps(event))
    client = boto3.client('apigatewaymanagementapi')
    
    route = event.requestContext.routeKey
    connectionId = event.requestContext.connectionId
    print('connectionId = '+ connectionId +" - Route = "+route)
    
    match route: #Python 3.10
        case "$connect":
            body = "Processing Get All Products"
    
        case "$disconnect":
            body = "Processing Get Product Id with "+ event["pathParameters"]["id"] 

        case _:
            body = "Unsupported route: "+ route

    return {
        'statusCode': 200,        
        'body': json.dumps(body)
    }

def send_ws_message(connection_id, body):
    if not isinstance(body, str):
        body = json.dumps(body)
    _send_to_connection(connection_id, body)

def _get_event_body(event):
    try:
        return json.loads(event.get("body", ""))
    except ValueError:
        print("event body could not be JSON decoded.")
        return {}
    
def _send_to_connection(connection_id, data):
    endpoint = os.environ['WEBSOCKET_API_ENDPOINT']
    gatewayapi = boto3.client("apigatewaymanagementapi", endpoint_url=endpoint)
    return gatewayapi.post_to_connection(ConnectionId=connection_id, Data=data.encode('utf-8'))
