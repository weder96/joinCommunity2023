# **CDK**

## CLI


npm install -g aws-cdk

mkdir my-cdk
cd my-cdk
cdk init app --language java


### Resources

https://cdkpatterns.com/

https://cdkworkshop.com/

https://github.com/aws/aws-cdk

https://github.com/aws-samples/aws-cdk-examples/tree/v2

https://hands-on.cloud/cdk-python-lambda-example/

https://es.slideshare.net/prorhap/aws-cdk-in-practice

https://github.com/kalaiser/awesome-cdk

https://medium.com/deepwatch-sec/using-the-aws-cdk-and-sdk-to-manage-our-cloud-infrastructure-across-teams-a02945200224

https://pages.awscloud.com/rs/112-TZM-766/images/B-3.pdf

https://bip.up.lublin.pl/rada/2021/cdk.pdf

https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-java.html

https://docs.aws.amazon.com/cdk/v2/guide/cli.html

https://docs.aws.amazon.com/cdk/v2/guide/serverless_example.html

https://blog.tericcabrel.com/aws-lambda-java-cdk/

https://hevodata.com/learn/aws-cdk-lambda/

https://www.youtube.com/watch?v=qM2kUO3WoJ8

https://bobbyhadz.com/blog/aws-cdk-iam-policy-example

https://github.com/ibrahimcesar/devops-extreme

https://ibrahimcesar.cloud/blog/do-zero-ao-salve-mundo-em-aws-cdk-cloud-development-kit/

https://cdk-advanced.workshop.aws/

https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html

https://github.com/awslabs/aws-solutions-constructs/tree/main/source/use_cases/aws-restaurant-management-demo

https://github.com/aws-samples/aws-cdk-constructs-for-java/tree/main

https://reflectoring.io/getting-started-with-aws-sqs/


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


### list Services Principal
a4b.amazonaws.com
access-analyzer.amazonaws.com
account.amazonaws.com
acm-pca.amazonaws.com
acm.amazonaws.com
airflow-env.amazonaws.com
airflow.amazonaws.com
alexa-appkit.amazon.com
alexa-connectedhome.amazon.com
amazonmq.amazonaws.com
amplify.amazonaws.com
apigateway.amazonaws.com
appflow.amazonaws.com
application-autoscaling.amazonaws.com
application-insights.amazonaws.com
appstream.amazonaws.com
appstream.application-autoscaling.amazonaws.com
appsync.amazonaws.com
athena.amazonaws.com
automation.amazonaws.com
autoscaling.amazonaws.com
aws-artifact-account-sync.amazonaws.com
backup.amazonaws.com
batch.amazonaws.com
billingconsole.amazonaws.com
braket.amazonaws.com
budgets.amazonaws.com
ce.amazonaws.com
channels.lex.amazonaws.com
chatbot.amazonaws.com
chime.amazonaws.com
cloud9.amazonaws.com
clouddirectory.amazonaws.com
cloudformation.amazonaws.com
cloudfront.amazonaws.com
cloudhsm.amazonaws.com
cloudsearch.amazonaws.com
cloudtrail.amazonaws.com
cloudwatch-crossaccount.amazonaws.com
codebuild.amazonaws.com
codecommit.amazonaws.com
codedeploy.${aws::region}.amazonaws.com
codedeploy.amazonaws.com
codeguru-reviewer.amazonaws.com
codepipeline.amazonaws.com
codestar-notifications.amazonaws.com
codestar.amazonaws.com
cognito-identity.amazonaws.com
cognito-idp.amazonaws.com
cognito-sync.amazonaws.com
comprehend.amazonaws.com
config-conforms.amazonaws.com
config-multiaccountsetup.amazonaws.com
config.amazonaws.com
connect.amazonaws.com
continuousexport.discovery.amazonaws.com
costalerts.amazonaws.com
custom-resource.application-autoscaling.amazonaws.com
databrew.amazonaws.com
datapipeline.amazonaws.com
datasync.amazonaws.com
dax.amazonaws.com
deeplens.amazonaws.com
delivery.logs.amazonaws.com
diode.amazonaws.com
directconnect.amazonaws.com
discovery.amazonaws.com
dlm.amazonaws.com
dms.amazonaws.com
ds.amazonaws.com
dynamodb.amazonaws.com
dynamodb.application-autoscaling.amazonaws.com
ec.amazonaws.com
ec2.amazonaws.com
ec2.application-autoscaling.amazonaws.com
ec2fleet.amazonaws.com
ec2scheduled.amazonaws.com
ecr.amazonaws.com
ecs-tasks.amazonaws.com
ecs.amazonaws.com
ecs.application-autoscaling.amazonaws.com
edgelambda.amazonaws.com
eks-fargate-pods.amazonaws.com
eks-fargate.amazonaws.com
eks-nodegroup.amazonaws.com
eks.amazonaws.com
elasticache.amazonaws.com
elasticbeanstalk.amazonaws.com
elasticfilesystem.amazonaws.com
elasticloadbalancing.amazonaws.com
elasticmapreduce.amazonaws.com
elastictranscoder.amazonaws.com
email.cognito-idp.amazonaws.com
emr-containers.amazonaws.com
es.amazonaws.com
events.amazonaws.com
firehose.amazonaws.com
fms.amazonaws.com
forecast.amazonaws.com
freertos.amazonaws.com
fsx.amazonaws.com
galaxy.amazonaws.com
gamelift.amazonaws.com
glacier.amazonaws.com
globalaccelerator.amazonaws.com
glue.amazonaws.com
greengrass.amazonaws.com
guardduty.amazonaws.com
health.amazonaws.com
honeycode.amazonaws.com
iam.amazonaws.com
imagebuilder.amazonaws.com
importexport.amazonaws.com
inspector.amazonaws.com
iot.amazonaws.com
iotanalytics.amazonaws.com
iotevents.amazonaws.com
iotsitewise.amazonaws.com
iotthingsgraph.amazonaws.com
ivs.amazonaws.com
jellyfish.amazonaws.com
kafka.amazonaws.com
kinesis.amazonaws.com
kinesis.{us-gov-region}.amazonaws.com
kinesisanalytics.amazonaws.com
kms.amazonaws.com
lakeformation.amazonaws.com
lambda.amazonaws.com
lex.amazonaws.com
license-manager.amazonaws.com
lightsail.amazonaws.com
logger.cloudfront.amazonaws.com
logs.amazonaws.com
machinelearning.amazonaws.com
macie.amazonaws.com
managedblockchain.amazonaws.com
managedservices.amazonaws.com
mediaconnect.amazonaws.com
mediaconvert.amazonaws.com
mediapackage.amazonaws.com
mediastore.amazonaws.com
mediatailor.amazonaws.com
member.org.stacksets.cloudformation.amazonaws.com
metering-marketplace.amazonaws.com
mgn.amazonaws.com
migrationhub.amazonaws.com
mobileanalytics.amazonaws.com
mobilehub.amazonaws.com
monitoring.amazonaws.com
monitoring.rds.amazonaws.com
mq.amazonaws.com
network-firewall.amazonaws.com
ops.apigateway.amazonaws.com
opsworks-cm.amazonaws.com
opsworks.amazonaws.com
organizations.amazonaws.com
personalize.amazonaws.com
pinpoint.amazonaws.com
polly.amazonaws.com
purchaseorders.amazonaws.com
qldb.amazonaws.com
quicksight.amazonaws.com
ram.amazonaws.com
rds-preview.amazonaws.com
rds.amazonaws.com
redshift.amazonaws.com
rekognition.amazonaws.com
replication.dynamodb.amazonaws.com
replicator.lambda.amazonaws.com
resource-groups.amazonaws.com
robomaker.amazonaws.com
route53.amazonaws.com
route53domains.amazonaws.com
route53resolver.amazonaws.com
s3.amazonaws.com
sagemaker.amazonaws.com
secretsmanager.amazonaws.com
securityhub.amazonaws.com
serverlessrepo.amazonaws.com
servicecatalog-appregistry.amazonaws.com
servicecatalog.amazonaws.com
servicediscovery.amazonaws.com
ses.amazonaws.com
shield.amazonaws.com
signer.amazonaws.com
signin.amazonaws.com
sms.amazonaws.com
sns.amazonaws.com
spotfleet.amazonaws.com
sqs.amazonaws.com
ssm-incidents.amazonaws.com
ssm.amazonaws.com
sso.amazonaws.com
states.amazonaws.com
storagegateway.amazonaws.com
streams.metrics.cloudwatch.amazonaws.com
sts.amazonaws.com
support.amazonaws.com
swf.amazonaws.com
tagging.amazonaws.com
tagpolicies.tag.amazonaws.com
textract.amazonaws.com
timestream.amazonaws.com
transcribe.amazonaws.com
transfer.amazonaws.com
transitgateway.amazonaws.com
translate.amazonaws.com
trustedadvisor.amazonaws.com
tts.amazonaws.com
vmie.amazonaws.com
vpc-flow-logs.amazonaws.com
waf-regional.amazonaws.com
waf.amazonaws.com
wam.amazonaws.com
workdocs.amazonaws.com
worklink.amazonaws.com
workmail.amazonaws.com
workspaces.amazonaws.com
xray.amazonaws.com
{region}.elasticache-snapshot.amazonaws.com