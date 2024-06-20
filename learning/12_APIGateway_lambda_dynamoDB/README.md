# Dynamodb

## CLI



### Zip file Linux

```
zip function.zip app.py

```

### Create function Lambda

```
aws lambda create-function \
    --function-name saveProduct \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

### **Create table DynamoBD**

```
aws dynamodb create-table \
    --table-name Order \
    --attribute-definitions \
        AttributeName=id,AttributeType=S \
        AttributeName=status,AttributeType=S \
    --key-schema \
        AttributeName=id,KeyType=HASH \
        AttributeName=status,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --table-class STANDARD
```


### **Create table DynamoBD**

```
aws dynamodb create-table \
    --table-name Order \
    --attribute-definitions \
        AttributeName=id,AttributeType=S \
        AttributeName=status,AttributeType=S \
    --key-schema \
        AttributeName=id,KeyType=HASH \
        AttributeName=status,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --table-class STANDARD
```

### **Describe table DynamoBD**

```
aws dynamodb describe-table --table-name Order
```


### **Call ApiGateway**

```
curl 'https://n0174xa836.execute-api.us-east-1.amazonaws.com/dev/product' \
-H 'Content-Type: application/json' \
-X GET
```

```
curl 'https://n0174xa836.execute-api.us-east-1.amazonaws.com/dev/product/10' \
-H 'Content-Type: application/json' \
-X GET
```

```
curl 'https://n0174xa836.execute-api.us-east-1.amazonaws.com/dev/product' \
-H 'Content-Type: application/json' \
-X POST \
-d '{ "name" : "Mouse","price": 230.45}'
```

```
curl 'https://n0174xa836.execute-api.us-east-1.amazonaws.com/dev/product/10' \
-H 'Content-Type: application/json' \
-X PUT \
-d '{ "name" : "Mouse","price": 230.45}'
```

```
curl 'https://n0174xa836.execute-api.us-east-1.amazonaws.com/dev/product/10' \
-H 'Content-Type: application/json' \
-X DELETE
```


### Resources

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Tools.CLI.html

https://docs.aws.amazon.com/code-library/latest/ug/python_3_dynamodb_code_examples.html


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