import json

def lambda_handler(event, context):    
    print('Starting input lambda function call Close Case')
    print(event)
     
    return {
        'statusCode': 200,
        'body': json.dumps('Close Case finish, Sucessfull !!!'),
        'Status': event["Status"]
    }
