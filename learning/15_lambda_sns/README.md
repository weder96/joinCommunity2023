# Lambda and SNS with Python


### Zip file Linux

```
zip function.zip app.py

```

### Create Lambda Function 

```
aws lambda create-function \
    --function-name snsTopic \
    --runtime python3.10 \
    --zip-file fileb://function.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```





## Delete function created
```
aws lambda delete-function --function-name snsTopic
```

### Resources

https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-api-permissions-reference.html

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/sns.html

https://docs.aws.amazon.com/code-library/latest/ug/python_3_sns_code_examples.html

https://hands-on.cloud/boto3-sns-tutorial/


```
sns:AddPermission 	            Grants permission to add permissions to the topic policy.
sns:DeleteTopic 	            Grants permission to delete a topic.
sns:GetDataProtectionPolicy 	Grants permission to retrieve a topic's data protection policy.
sns:GetTopicAttributes 	        Grants permission to receive all of the topic attributes.
sns:ListSubscriptionsByTopic 	Grants permission to retrieve all the subscriptions to a specific topic.
SNS:ListTagsForResource 	    Grants permission to list all tags added to a specific topic.
sns:Publish 	                Grants permission to both publish and publish batch to a topic or endpoint. For more information, see Publish and PublishBatch in the Amazon Simple Notification Service API Reference.
sns:PutDataProtectionPolicy 	Grants permission to set a topic's data protection policy.
sns:RemovePermission 	        Grants permission to remove any permissions in the topic policy.
sns:SetTopicAttributes 	        Grants permission to set a topic's attributes.
sns:Subscribe 	                Grants permission to subscribe to a topic.
```

 	                