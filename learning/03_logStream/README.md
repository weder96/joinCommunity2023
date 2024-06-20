# Sum Two Numbers Lambda with Python


### Zip file Linux

```
zip function.zip app.py

```

### Create Lambda Function 

```
aws lambda create-function \
    --function-name logStream \
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
aws lambda get-function --function-name logStream
```

------------------------------------------------------------------------
### Execute lambda function 

```
aws lambda invoke --function-name logStream --cli-binary-format raw-in-base64-out --payload file://event.json response.json
aws lambda invoke --function-name logStream --cli-binary-format raw-in-base64-out --payload file://event.json out --log-type Tail
aws lambda invoke \
    --function-name logStream \
    --cli-binary-format raw-in-base64-out \
    --payload file://event.json out \
    --log-type Tail \
    --query 'LogResult' \
    --output text \
    --cli-binary-format raw-in-base64-out | base64 \
    --decode
```

------------------------------------------------------------------------
### Read file response.json

 ```
 cat response.json
 ```



## Delete function created
```
aws lambda delete-function --function-name logStream
```

### Resources

https://docs.aws.amazon.com/pt_br/lambda/latest/dg/monitoring-cloudwatchlogs.html