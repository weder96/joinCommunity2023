import json

def lambda_handler(event, context):  
    print(event)
    
    message = 'Hello From Lambda by API Gateway CLI Commands!!!' 
    
    return {
        'statusCode': 200,        
        'body': json.dumps(message),
    }
