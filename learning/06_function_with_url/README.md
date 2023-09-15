# Sum Two Numbers Lambda with Python


### Zip file Linux

```
zip function.zip app.py

```

### Create Lambda Function 

```
aws lambda create-function \
    --function-name helloWorldWithUrl \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

```
aws lambda add-permission \
    --function-name helloWorldWithUrl \
    --action lambda:InvokeFunctionUrl \
    --principal "*" \
    --function-url-auth-type "NONE" \
    --statement-id url
```


```
aws lambda create-function-url-config \
    --function-name helloWorldWithUrl \
    --auth-type NONE
```


### Execute lambda function 

```
curl 'https://enuilgzlnkex5k7gnazmg5vlju0qzxfs.lambda-url.us-east-1.on.aws/' \
-H 'Content-Type: application/json' \
-d '{"num1": "10", "num2": "10"}'
```


### Check if exists function

```
aws lambda list-functions
```

```
aws lambda list-functions --max-items 10
```

```
aws lambda get-function --function-name helloWorldWithUrl
```


## Delete function created
```
aws lambda delete-function --function-name helloWorldWithUrl
```

### Resources

https://docs.aws.amazon.com/lambda/latest/dg/urls-tutorial.html