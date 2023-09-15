import json

def lambda_handler(event, context):  
    print('Received event:',json.dumps(event))
    
    message = 'Hello From Lambda!!!' 
    
    match event["routeKey"]: #Python 3.10
        case "GET /product":
            body = "Processing Get All Products"
    
        case "GET /product/{id}":
            body = "Processing Get Product Id with "+ event["pathParameters"]["id"] 
                    
        case "POST /product":
            payload = event["body"]
            body = "Processing Post Product Id with "+ payload
                    
        case "DELETE /product/{id}":
            body = "Processing Delete Product Id with "+event["pathParameters"]["id"]
                    
        case _:
            body = "Unsupported route: "+ event["routeKey"];

    return {
        'statusCode': 200,        
        'body': json.dumps(body)
    }
