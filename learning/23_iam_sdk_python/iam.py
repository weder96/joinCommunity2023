import boto3
import json 

iam = boto3.client('iam')

role_policy = {
"Version": "2012-10-17",
"Statement": [
    {
    "Sid": "",
    "Effect": "Allow",
    "Principal": {
        "Service": "states.amazonaws.com"
    },
    "Action": "sts:AssumeRole"
    }
]
}

response = iam.create_role(
RoleName='StepFunctionLambdaBasicExecution',
AssumeRolePolicyDocument=json.dumps(role_policy),
)

attach_policy_response = iam.attach_role_policy(
    RoleName='StepFunctionLambdaBasicExecution',
    PolicyArn='arn:aws:iam::aws:policy/service-role/AWSLambdaRole'
)

print(response)
print(attach_policy_response)