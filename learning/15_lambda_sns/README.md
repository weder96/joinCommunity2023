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


### Create a topic
**To create a topic, use the sns create-topic command and specify the name to assign to the topic.**

```
aws sns create-topic --name my-topic
```

### Subscribe to a topic
**To subscribe to a topic, use the sns subscribe command.**
**The following example specifies the email protocol and an email address for the notification-endpoint.**

```
aws sns subscribe --topic-arn arn:aws:sns:us-east-1:710304818543:my-topic --protocol email --notification-endpoint wsousa@handson.sns.com
```

### Publish to a topic
**To send a message to all subscribers of a topic, use the sns publish command.**
**The following example sends the message "Hello World!" to all subscribers of the specified topic.**

```
aws sns publish --topic-arn arn:aws:sns:us-east-1:710304818543:my-topic --message "Hello World!"

aws sns publish --topic-arn arn:aws:sns:us-east-1:710304818543:MyStack-mytopic2B0AD69A3-GkpvSFy2In50 --message "Hello World!"

aws sns publish --topic-arn arn:aws:sns:us-east-1:710304818543:MyStack-mytopic2B0AD69A3-DeewkGb6bv6j --message "Hello World !!!"

{"message": "teste sns to sqs to lambda"}

```

### Unsubscribe from a topic
**To unsubscribe from a topic and stop receiving messages published to that topic, use the sns unsubscribe command and specify the ARN of the topic** 
**you want to unsubscribe from.**
```
aws sns unsubscribe --subscription-arn arn:aws:sns:us-east-1:710304818543:my-topic:81ca7760-aa69-56a4-aea5-2ae09660b4a5
```


### list-subscriptions
**To verify that AWS successfully deleted the topic, use the sns list-topics command to confirm that the topic no longer appears in the list.**
```
aws sns list-subscriptions
```

### list-topics
```
aws sns list-topics
```

### Delete a topic
**To delete a topic, run the sns delete-topic command.**
```
aws sns delete-topic --topic-arn arn:aws:sns:us-east-1:710304818543:my-topic
```

## Delete function created
```
aws lambda delete-function --function-name snsTopic
```

### Resources

https://docs.aws.amazon.com/sns/latest/dg/sns-access-policy-language-api-permissions-reference.html

https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

https://docs.aws.amazon.com/cli/latest/userguide/cli-services-sns.html

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

 	                