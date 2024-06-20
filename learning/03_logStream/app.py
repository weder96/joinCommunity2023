import json

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)
    total = event['num1'] * event['num2'];
    message = 'The total of {} and {} is {}'.format(event['num1'], event['num2'], total)    

    return {
        'statusCode': 200,
        "headers": {"Content-Type": "application/json"},
        'body': json.dumps(message)
    }
