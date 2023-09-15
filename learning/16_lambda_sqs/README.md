# Lambda and SQS with Python


### Zip file Linux

```
zip function.zip app.py

```

### **Create Lambda Function**

### Create Queue 
```
aws lambda create-function \
    --function-name createQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler createQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

### Create Queue FIFO
```
aws lambda create-function \
    --function-name createQueueFifo \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler createQueueFifo.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


### List Queues

```
aws lambda create-function \
    --function-name listQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler listQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

### List Queues

```
aws lambda create-function \
    --function-name filterQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler filterQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


### Get Queues by Url

```
aws lambda create-function \
    --function-name getQueueByUrl \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler getQueueByUrl.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

### list Dead LetterQueue Queues by Url

```
aws lambda create-function \
    --function-name listDeadLetterQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler listDeadLetterQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


### Delete Queues by Url

```
aws lambda create-function \
    --function-name deleteQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler deleteQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

### Purge Queues by Url

```
aws lambda create-function \
    --function-name purgeQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler purgeQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


### Set Queues Atributes

```
aws lambda create-function \
    --function-name setQueueAtributes \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler setQueueAtributes.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


### Send Message Queues 

```
aws lambda create-function \
    --function-name sendMessageQueue \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler sendMessageQueue.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

------------------------------------------------------------------------------------------------------

### Command Line Interface

```
aws sqs create-queue --queue-name cli-queue-attr --attributes file://q-attributes.json
```


```
aws sqs get-queue-attributes --queue-url https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr --attribute-names All
```


### Sending Messages to our AWS SQS Queue
```
aws sqs send-message --queue-url https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr --message-body "IOT-45 Temp: 52C"
```

### Reading Messages from the AWS SQS Queue
```
aws sqs --region us-east-1 receive-message --queue-url https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr
```

### Deletion of a Processed Message from the AWS SQS Queue
```
aws sqs --region us-east-1 delete-message --queue-url https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr --receipt-handle "AQEBKAlDjQqe3Q7BpMLSsPyPu6aC/JfcDjbZzj6i/ibfu3pGYPd25DzZq1JJz05GhrJkXSydxqFbAw8oTuqndY77OgGr7aWvcozbnv9Pfx3NtXgZzUHqnrxtzXMGmqqpx+Y8Rb9s/39R77Ds4PoO4SLoE9cUWv+qXUQjgVe8l/YUQAXOorNXgjZajXehGzHC6V9eKWxlLgKKoA3g1PqmYRgww4cOElbXwS+gI0u4cGJp2CVWn8JjvReGGDSG4E8gniD+UkJ+F8YxE+o4MM3Vx3TOoDVtAmxb4sRft3GMsA+u2Xepwka15i97ujk5w+2IFW/WvSnzTZ/hkYWBr2J1VY3ucoenyZb70WREl/cWhhAAcXNVfeEuwOWhb3+UZMKrN0Bvr4NWaL1cieQ4Qk37cCkwEg=="
```

### Cleaning Up

```
aws sqs --region us-east-1 delete-queue --queue-url https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr
```


## **Get message with long polling**

### Empty Q1
```
aws sqs purge-queue  --queue-url https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr 
```

### Confirm empty
```
aws sqs receive-message  --queue-url  https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr --output json
```

### long poll
```
aws sqs receive-message  --queue-url  https://sqs.us-east-1.amazonaws.com/710304818543/cli-queue-attr --output json --wait-time-seconds  10
```

### send from other terminal:
```
aws sqs send-message --queue-url https://eu-west-1.queue.amazonaws.com/069157535684/dev1-tom-test1 --message-body "Test message from other window"
```

-------------------------------------------------------------------------------------------------------------------------------

## Delete function created
```
aws lambda delete-function --function-name sqsQueue
```

### Resources

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sqs.html

https://docs.aws.amazon.com/code-library/latest/ug/python_3_sqs_code_examples.html

https://iam.cloudonaut.io/reference/sqs.html

https://hands-on.cloud/boto3-sqs-tutorial/

https://hands-on.cloud/aws-sqs-getting-started-guide/

https://www.learnaws.org/2020/12/17/aws-sqs-boto3-guide/

https://stackoverflow.com/questions/42809096/difference-in-boto3-between-resource-client-and-session

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/resources.html

https://boto3.amazonaws.com/v1/documentation/api/latest/guide/clients.html

https://gist.github.com/AstroTom/4c81c629a68252e6f0be176ecf131c4a

https://medium.com/@schogini/aws-cli-and-sqs-a-tiny-demonstration-18e7136d0258





sqs:AddPermission 
sqs:ChangeMessageVisibility 
sqs:CreateQueue 
sqs:DeleteMessage 
sqs:DeleteQueue 
sqs:GetQueueAttributes 
sqs:GetQueueUrl 
sqs:ListDeadLetterSourceQueues 
sqs:ListQueues 
sqs:PurgeQueue 
sqs:ReceiveMessage 
sqs:RemovePermission 
sqs:SendMessage 
sqs:SetQueueAttributes 
sqs:TagQueue 


