# Hello World Lambda with Python

###  Check version aws installed at your machine

```
aws --version
```


### Create Execution Role for AWS Lambda functions with AWS CLI
```
aws iam create-role --role-name lambda-role-py --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```

### attach-role AWSLambdaBasicExecutionRole managed policy:

```
aws iam attach-role-policy --role-name lambda-role-py --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

### Zip file Linux

```
zip function.zip app.py

```
### Create AWS Lambda function with .zip file using AWS CLI

### **Get Role:**

```
aws iam get-role --role-name lambda-role-py
```
```
arn:aws:iam::710304818543:role/lambda-role-py
```

Run Command:

```
aws lambda create-function \
    --function-name helloWorld \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


### Update function add variables environment

```
aws lambda update-function-configuration --function-name helloWorld --environment "Variables={BUCKET=my-bucket,KEY=file.txt}"
```

```
aws lambda get-function-configuration --function-name helloWorld
```

### Update function new file generated and changed function lambda

```
aws lambda update-function-code --function-name helloWorld --zip-file fileb://function.zip
```