# **Step Functions**

## CLI

### **create-state-machine**
```
aws stepfunctions create-state-machine \
	--name HasCreateCliStateMachine \
	--definition "file://stateMachineDefinition.json" \
	--role-arn arn:aws:iam::710304818543:role/service-role/StepFunctions-HelloWorld-role-6df6dc83
```

### **list state machines**
```
aws stepfunctions list-state-machines
```


### **Execute state machines**
```
aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-east-1:710304818543:stateMachine:HasCreateCliStateMachine --input "file://input.json"
```


### **Execute state machines**
```
aws stepfunctions delete-state-machine --state-machine-arn  arn:aws:states:us-east-1:710304818543:stateMachine:HelloWorld
```


### **Execute Hello  World State machine**

```
aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-east-1:710304818543:stateMachine:HelloWorld --input "file://input.json"
```

### Access folder "stepFunctionsWithLambda"

### Zip file Linux

```
zip appCloseCase.zip appCloseCase.py
zip helloWorldStepFunctions.zip app.py

```

```
aws lambda create-function \
    --function-name closeCaseStepFunction \
    --runtime python3.10 \
    --zip-file fileb://appCloseCase.zip \
    --handler appCloseCase.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```

```
aws lambda create-function \
    --function-name helloWorldStepFunctions \
    --runtime python3.10 \
    --zip-file fileb://helloWorldStepFunctions.zip \
    --handler app.lambda_handler \
    --role arn:aws:iam::710304818543:role/lambda-role-py
```



### **create-state-machine acess lambda function**
```
aws stepfunctions create-state-machine \
	--name HasStateMachineLambda \
	--definition "file://stateMachineDefinitionWithLambda.json" \
	--role-arn arn:aws:iam::710304818543:role/service-role/StepFunctions-HelloWorld-role-6df6dc83
```

### **update-state-machine acess lambda function**
```
aws stepfunctions update-state-machine \
	--state-machine-arn arn:aws:states:us-east-1:710304818543:stateMachine:HasStateMachineLambda \
	--definition "file://stateMachineDefinitionWithLambda.json" \
	--role-arn arn:aws:iam::710304818543:role/service-role/StepFunctions-HelloWorld-role-6df6dc83
```


### **Execute state machines**
```
aws stepfunctions start-execution --state-machine-arn arn:aws:states:us-east-1:710304818543:stateMachine:HasStateMachineLambda --input "file://stepFunctionsWithLambda/inputWithLambda.json"
```

### Resources

https://docs.aws.amazon.com/cli/latest/reference/stepfunctions/update-state-machine.html

https://github.com/aws-samples/step-functions-workflows-collection

https://hands-on.cloud/boto3-step-functions-tutorial/

https://www.appsloveworld.com/aws-cli/1/how-to-stop-all-running-step-functions-of-a-specific-state-machine

https://github.com/rlondner/aws-stepfunctions-samples/tree/master

https://aws.amazon.com/pt/blogs/architecture/category/application-services/aws-step-functions/

https://serverlessland.com/patterns?services=sfn

https://blog.it-playground.eu/aws-step-functions-for-networkers-the-cli-approach/

https://aws.amazon.com/pt/blogs/compute/aws-step-functions-support-in-visual-studio-code



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