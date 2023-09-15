import json

def lambda_handler(event, context):            
    message = 'Hello From Lambda!!!' 

    return {
        'statusCode': 200,        
        'body': json.dumps(message)
    }
