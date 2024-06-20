# EventBridge

## CLI

### **Amazon EventBridge**

Amazon EventBridge - Developing with AWS SDK

---
EventBridge Client - AWS SDK for Python Boto3

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/events.html


Commands :
	PutEventsCommand
	PutRuleCommand
	PutTargetsCommand


------------------------------------------------------------------------------------------------------------------
## **Event Bridge CLI Commands**

### Create an event bus

aws events create-event-bus --name "event-bridge-demo"


## **Create Role for EventBridge Event**

### Create Execution Role for AWS Lambda functions with AWS CLI

```
aws iam create-role --role-name eventbridge-role-py --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": ["lambda.amazonaws.com", "events.amazonaws.com"]}, "Action": "sts:AssumeRole"}]}'
```


### create a lambda function to invoke

```
aws iam create-role --role-name "eventbridge-role-py" --assume-role-policy-document "file://cli/policy.json"
```

```
aws iam attach-role-policy \
    --role-name "eventbridge-role-py" \
    --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
```


--------------------------------------------------------------------------------------------------------------------

### Zip file Linux

```
zip -j "function.zip" "./backend/app.py"

```


### Create Lambda Function with role

Run Command:

```
aws lambda create-function \
    --function-name putEvent \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/eventbridge-role-py
```

# create a rule with lambda function as the target

```
aws events put-rule \
    --name "log-event" \
    --event-bus-name "event-bridge-demo" \
    --event-pattern "file://cli/pattern.json"
```

```
aws events put-targets \
    --event-bus-name "event-bridge-demo" \
    --rule "log-event" \
    --targets "[{\"Id\":\"1\",\"Arn\":\"arn:aws:lambda:${REGION}:${ACCOUNT}:function:event-logger\"}]"
```


```
aws events put-targets \
    --event-bus-name "event-bridge-demo" \
    --rule "log-event" \
    --targets "[{\"Id\":\"1\",\"Arn\":\"arn:aws:lambda:us-east-1:710304818543:function:putEvent\"}]"
```

```
aws lambda add-permission \
    --function-name "event-logger" \
    --statement-id "log-event" \
    --action "lambda:InvokeFunction" \
    --principal "events.amazonaws.com" \
    --source-arn "arn:aws:events:${REGION}:${ACCOUNT}:rule/event-bridge-demo/log-event"
```

```
aws lambda add-permission \
    --function-name "putEvent" \
    --statement-id "log-event" \
    --action "lambda:InvokeFunction" \
    --principal "events.amazonaws.com" \
    --source-arn "arn:aws:events:us-east-1:710304818543:rule/event-bridge-demo/log-event"
```

# test the event patterns

```
aws events test-event-pattern \
    --event-pattern "file://cli/pattern.json" \
    --event "file://cli/events/hello.json"
```

```
aws events test-event-pattern \
    --event-pattern "file://cli/pattern.json" \
    --event "file://cli/events/wrong_source.json"
```

# send events to your bus
```
aws events put-events \
    --entries "file://cli/entries.json"
```

# **Cleaning Up**

### To clean up the resources, you can use these commands:

```
aws lambda remove-permission \
    --function-name "event-logger" \
    --statement-id "log-event"
```
```
aws events remove-targets \
    --event-bus-name "event-bridge-demo" \
    --rule "log-event" \
    --ids "1"
```

```
aws events delete-rule \
    --name "log-event" \
    --event-bus-name "event-bridge-demo"
```

```
aws lambda delete-function \
    --function-name "putEvent"
```

```
aws iam detach-role-policy \
    --role-name "lambda-cli-role" \
    --policy-arn "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
```

```
aws iam delete-role \
    --role-name "lambda-cli-role"
```

```
aws events delete-event-bus \
    --name "event-bridge-demo"
```

### Resources

https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/index.html#cli-aws-events

https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/list-event-buses.html

https://hands-on.cloud/eventbridge-building-loosely-coupled-event-drivent-serverless-architectures/

https://github.com/cuperman/event-bridge-demo/tree/master

###  Multiline char 
---
```
	for windows = `
	for mac or linux = \
```

### **Install Boto3**

```
pip install boto3

```