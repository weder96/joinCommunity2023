import json

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
     
    return {
        'statusCode': 200,
        'body': json.dumps('Hello World from Lambda!!!')
    }
