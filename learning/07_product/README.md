# API Lambda(URL) with Python 



### Zip file Linux

```
zip function.zip app.py

```

### Create Lambda Function 

```
aws lambda create-function \
    --function-name crudProduct \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```


```
aws lambda add-permission \
    --function-name crudProduct \
    --action lambda:InvokeFunctionUrl \
    --principal "*" \
    --function-url-auth-type "NONE" \
    --statement-id url
```


```
aws lambda create-function-url-config \
    --function-name crudProduct \
    --auth-type NONE
```


### Execute lambda function 

### **Method Get**

```
curl 'https://7zm3rort2ouvghscruinhot5aq0kdudh.lambda-url.us-east-1.on.aws/product' \
-H 'Content-Type: application/json' \
-X GET 
```

### **Method Get by id**

```
curl 'https://7zm3rort2ouvghscruinhot5aq0kdudh.lambda-url.us-east-1.on.aws/product/10' \
-H 'Content-Type: application/json' \
-X GET 
```

### **Method POST by id**

```
curl 'https://7zm3rort2ouvghscruinhot5aq0kdudh.lambda-url.us-east-1.on.aws/product' \
-H 'Content-Type: application/json' \
-X POST \
-d '{ "name" : "Mouse","price": 230.45}'
```

### **Method PUT by id**

```
curl 'https://7zm3rort2ouvghscruinhot5aq0kdudh.lambda-url.us-east-1.on.aws/product' \
-H 'Content-Type: application/json' \
-X PUT \
-d '{ "name" : "Mouse","price": 230.45}'



### **Method delete by id**

```
curl 'https://7zm3rort2ouvghscruinhot5aq0kdudh.lambda-url.us-east-1.on.aws/product/10' \
-H 'Content-Type: application/json' \
-X DELETE
```

### Delete lambda function 

```
aws lambda delete-function --function-name crudProduct
```

