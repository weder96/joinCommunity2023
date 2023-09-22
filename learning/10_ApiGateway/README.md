# API Gateway

## CLI


### Create a role

We use the [create-role](https://docs.aws.amazon.com/cli/latest/reference/iam/create-role.html) command :


### create the lambda role

```
aws iam create-role --role-name apigw-lambda-role-py --assume-role-policy-document 'file://lambda-role-policy.json' --query 'Role.Arn' --output text
```
**Or**

```
aws iam create-role --role-name apigw-lambda-role-py --assume-role-policy-document '{"Version": "2012-10-17","Statement": [{ "Effect": "Allow", "Principal": {"Service": "lambda.amazonaws.com"}, "Action": "sts:AssumeRole"}]}'
```


### Attach the execution policy to it

### We use the attach-role-policy command :

### attach the `AWSLambdaBasicExecutionRole` policy to the lambda role
### attach-role AWSLambdaBasicExecutionRole managed policy:

```
aws iam attach-role-policy --role-name apigw-lambda-role-py  --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```


### Zip file Linux

```
zip function.zip app.py

```
### Create AWS Lambda function with .zip file using AWS CLI

### **Get Role:**

```
aws iam get-role --role-name apigw-lambda-role-py
```

**response**

```
arn:aws:iam::710304818543:role/apigw-lambda-role-py
```

### Create Function lambda
Run Command:

```
aws lambda create-function \
    --function-name apiGwLambda \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/apigw-lambda-role-py
```
---------------------------------------------------------------------------------------------------------

### Create the API Gateway
**To create an API Gateway and connect it whith the Lambda we need to :**

We use the [create-rest-api](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-rest-api.html) command :


```
 aws apigateway create-rest-api \
    --region $AWS_REGION \
    --name $API_GATEWAY_NAME \
    --endpoint-configuration types=REGIONAL \
    --description 'A test API'
```

```
aws apigateway create-rest-api \
    --name 'Simple API Gateway (AWS CLI, Regional)' \
    --description 'Simple regional API Gateway' \
    --region us-east-1 \
    --endpoint-configuration '{ "types": ["REGIONAL"] }'
```

![API](https://github.com/weder96/joinCommunity2023/blob/main/learning/10_ApiGateway/assets/api.png)

---------------------------------------------------------------------------------------------------------

### Create the resource

We use the [create-resource](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-resource.html) command :

### create the `API_GATEWAY_RESOURCE_NAME` resource path

```
aws apigateway create-resource \
    --region $AWS_REGION \
    --rest-api-id $API_GATEWAY_ID \
    --parent-id $API_GATEWAY_ROOT_RESOURCE_ID \
    --path-part $API_GATEWAY_RESOURCE_NAME
```

```
aws apigateway create-resource \
    --region us-east-1 \
    --rest-api-id t15lo725gb \
    --parent-id 1mrgaba6c4 \
    --path-part 'items'
```

![Resources](https://github.com/weder96/joinCommunity2023/blob/main/learning/10_ApiGateway/assets/resources.png)


---------------------------------------------------------------------------------------------------------

### Create the POST method

We will associate the POST method with our resource. And we’re going to attach the Lambda function to it.

We use the put-method command :

```
aws apigateway put-method \
    --region $AWS_REGION \
    --rest-api-id $API_GATEWAY_ID \
    --resource-id $API_GATEWAY_RESOURCE_ID \
    --http-method POST \
    --authorization-type NONE
```

```
aws apigateway put-method \
    --region us-east-1 \
    --rest-api-id t15lo725gb \
    --resource-id 1mrgaba6c4 \
    --http-method POST \
    --authorization-type NONE
```



---------------------------------------------------------------------------------------------------------

### setup the POST method integration request

```
 aws apigateway put-integration \
    --region  us-east-1 \
    --rest-api-id t15lo725gb \
    --resource-id 1mrgaba6c4 \
    --http-method POST \
    --integration-http-method POST \
    --type AWS_PROXY \
    --uri "arn:aws:apigateway:us-east-1:lambda:path/2015-03-31/functions/arn:aws:lambda:us-east-1:710304818543:function:apiGwLambda/invocations"
```

### add lambda permission
```
aws lambda add-permission \
    --region $AWS_REGION \
    --function-name $LAMBDA_FUNCTION_NAME \
    --source-arn "$API_GATEWAY_ARN/*/POST/$API_GATEWAY_RESOURCE_NAME" \
    --principal apigateway.amazonaws.com \
    --statement-id $STATEMENT_ID \
    --action lambda:InvokeFunction
```

```
aws lambda add-permission \
    --region us-east-1  \
    --function-name apiGwLambda \
    --statement-id apigateway-dev \
    --action lambda:InvokeFunction \
    --principal apigateway.amazonaws.com \
    --source-arn "arn:aws:execute-api:us-east-1:710304818543:t15lo725gb/*/*/"
```

---------------------------------------------------------------------------------------------------------

### To complete the process, we need to setup the method response.

We use the [put-method-response](https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-method-response.html) command :

### setup the POST method responses (method + integration response)

```
aws apigateway put-method-response \
    --region $AWS_REGION \
    --rest-api-id $API_GATEWAY_ID \
    --resource-id $API_GATEWAY_RESOURCE_ID \
    --http-method POST \
    --status-code 200 \
    --response-models '{"application/json": "Empty"}'
```

### execute

```
aws apigateway put-method-response \
    --region us-east-1 \
    --rest-api-id t15lo725gb \
    --resource-id 1mrgaba6c4 \
    --http-method POST \
    --status-code 200 \
    --response-models '{"application/json": "Empty"}'
```


```
aws apigateway put-integration-response \
    --region $AWS_REGION \
    --rest-api-id $API_GATEWAY_ID \
    --resource-id $API_GATEWAY_RESOURCE_ID \
    --http-method POST \
    --status-code 200 --selection-pattern ''
```

### execute


```
aws apigateway put-integration-response \
    --region us-east-1 \
    --rest-api-id t15lo725gb \
    --resource-id 1mrgaba6c4 \
    --http-method POST \
    --status-code 200 --selection-pattern ''
```

![Intregrations](https://github.com/weder96/joinCommunity2023/blob/main/learning/10_ApiGateway/assets/rest-api-id.png)

---------------------------------------------------------------------------------------------------------

### Deploy the API


**We can now deploy the API Gateaway and test it with curl. **

We use the [create-deployment](https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-deployment.html) command :

### publish the API, create the `dev` stage

```
aws apigateway create-deployment \
    --region us-east-1 \
    --rest-api-id t15lo725gb \
    --stage-name dev
```

![Stage](https://github.com/weder96/joinCommunity2023/blob/main/learning/10_ApiGateway/assets/stage_url.png)

### it works !
```
curl --request POST https://t15lo725gb.execute-api.us-east-1.amazonaws.com/dev
```

---------------------------------------------------------------------------------------------------------

### If we want to clear everything we have created, we have to use these commands :

[delete-rest-api](https://docs.aws.amazon.com/cli/latest/reference/apigateway/delete-rest-api.html)

### delete the API Gateway 
```
aws apigateway delete-rest-api \
    --region $AWS_REGION \
    --rest-api-id $API_GATEWAY_ID
```

### Excute
```
aws apigateway delete-rest-api \
    --region us-east-1 \
    --rest-api-id t15lo725gb
    
```

---------------------------------------------------------------------------------------------------------

[delete-function](https://docs.aws.amazon.com/cli/latest/reference/lambda/delete-function.html)

### delete the Lambda

```
aws lambda delete-function \
    --region $AWS_REGION \
    --function-name $LAMBDA_FUNCTION_NAME
```


### Execute

```
aws lambda delete-function \
    --region us-east-1 \
    --function-name apiGwLambda
```

---------------------------------------------------------------------------------------------------------

[detach-role-policy](https://docs.aws.amazon.com/cli/latest/reference/iam/detach-role-policy.html)

### to delete the role, you must detach policy first

```
aws iam detach-role-policy \
    --role-name $LAMBDA_ROLE_NAME \
    --policy-arn $LAMBDA_POLICY_ARN
```

### Execute


```
aws iam detach-role-policy \
    --role-name apigw-lambda-role-py  \
    --policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole
```

---------------------------------------------------------------------------------------------------------

[delete-role](https://docs.aws.amazon.com/cli/latest/reference/iam/delete-role.html)
### delete the role

```
aws iam delete-role \
    --role-name $LAMBDA_ROLE_NAME
```

### Execute

```
aws iam delete-role \
    --role-name apigw-lambda-role-py 
```

---------------------------------------------------------------------------------------------------------
### Resources

https://docs.aws.amazon.com/pt_br/apigateway/latest/developerguide/create-regional-api.html

https://docs.aws.amazon.com/lambda/latest/dg/services-apigateway.html

https://dashbird.io/knowledge-base/api-gateway/what-is-aws-api-gateway/

https://docs.aws.amazon.com/cli/latest/reference/apigateway/create-deployment.html

https://docs.aws.amazon.com/cli/latest/reference/apigateway/put-method-response.html

https://jeromedecoster.github.io/aws/api-gateway--lambda--aws-cli/



###  Multiline char 
---
```
	for windows = `
	for mac or linux = \
```

### **Install Boto3**

```
pip install boto3
