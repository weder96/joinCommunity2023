import json

def lambda_handler(event, context):  
    print('Received event:',json.dumps(event))
        
    method = event["requestContext"]["http"]["method"]
    path = event["requestContext"]["http"]["path"]    

    match method+" "+path:
        case "GET /product":
            body = "Processing Get All Products"
    
        case "GET /product/10":
            body = "Processing Get Product Id with "+path
                    
        case "POST /product":
            payload = event["body"]
            body = "Processing Post Product Id with "+ payload
                    
        case "DELETE /product/10":
            body = "Processing Delete Product Id with "+event["rawPath"]
                    
        case _:
            body = "Unsupported route: "+ json.dumps(event)

    return {
        'statusCode': 200,        
        'body': json.dumps(body)
    }