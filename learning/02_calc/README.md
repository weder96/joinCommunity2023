# Sum Two Numbers Lambda with Python


### Zip file Linux

```
zip function.zip app.py

```

### **Get Role:**

```
aws iam get-role --role-name lambda-role-py
aws iam get-role --role-name lambda-ex
```


### Create Lambda Function 

```
aws lambda create-function \
    --function-name calculator \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

### Check if exists function

```
aws lambda list-functions
```

```
aws lambda list-functions --max-items 10
```

```
aws lambda get-function --function-name calculator
```

------------------------------------------------------------------------
### Execute lambda function 

```
aws lambda invoke --function-name calculator --cli-binary-format raw-in-base64-out --payload file://event.json response.json
```

------------------------------------------------------------------------
### Read file response.json

 ```
 cat response.json
 ```



## Delete function created
```
aws lambda delete-function --function-name calculator
```

### Check if exists function (Error Not found)


```
aws lambda get-function --function-name calculator
```

An error occurred (ResourceNotFoundException) when calling the GetFunction operation: Function not found: arn:aws:lambda:{REGION}:{USERID}:function:calculator