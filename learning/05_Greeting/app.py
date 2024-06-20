import json

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
times = ['Morning', 'Afternoon', 'Evening', 'Night', 'Day']

def lambda_handler(event, context):    
    print('Starting input lambda function call')
    print(event)

    name = 'you' if event['name'] is None else event['name']
    city = 'World' if event['city'] is None else event['city']
    time = 'day' if times.index(event['time']) < 0 else event['time']
    day = '' if days.index(event['day']) < 0 else event['day']

    
    greeting = 'Good ' + time + ', ' + name + ' of ' + city + '. ' + 'Happy ' + day + ' !'

    
    print('Message: ' + greeting)

    return {
        'statusCode': 200,
        "headers": {"Content-Type": "application/json"},
        'body': json.dumps(greeting)
    }

