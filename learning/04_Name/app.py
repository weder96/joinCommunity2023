import json

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    
    message = 'Hello {} {}!'.format(event['first_name'], event['last_name']) 

    return {
        'statusCode': 200,
        "headers": {"Content-Type": "application/json"},
        'body': json.dumps(message)
    }
