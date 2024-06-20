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
a4b.amazonaws.com <br/>
access-analyzer.amazonaws.com <br/>
account.amazonaws.com <br/>
acm-pca.amazonaws.com <br/>
acm.amazonaws.com <br/>
airflow-env.amazonaws.com <br/>
airflow.amazonaws.com <br/>
alexa-appkit.amazon.com <br/>
alexa-connectedhome.amazon.com <br/>
amazonmq.amazonaws.com <br/>
amplify.amazonaws.com <br/>
apigateway.amazonaws.com <br/>
appflow.amazonaws.com <br/>
application-autoscaling.amazonaws.com <br/>
application-insights.amazonaws.com <br/>
appstream.amazonaws.com <br/>
appstream.application-autoscaling.amazonaws.com <br/>
appsync.amazonaws.com <br/>
athena.amazonaws.com <br/>
automation.amazonaws.com <br/>
autoscaling.amazonaws.com <br/>
aws-artifact-account-sync.amazonaws.com <br/>
backup.amazonaws.com <br/>
batch.amazonaws.com <br/>
billingconsole.amazonaws.com <br/>
braket.amazonaws.com <br/>
budgets.amazonaws.com <br/>
ce.amazonaws.com <br/>
channels.lex.amazonaws.com <br/>
chatbot.amazonaws.com <br/>
chime.amazonaws.com <br/>
cloud9.amazonaws.com <br/>
clouddirectory.amazonaws.com <br/>
cloudformation.amazonaws.com <br/>
cloudfront.amazonaws.com <br/>
cloudhsm.amazonaws.com <br/>
cloudsearch.amazonaws.com <br/>
cloudtrail.amazonaws.com <br/>
cloudwatch-crossaccount.amazonaws.com <br/>
codebuild.amazonaws.com <br/>
codecommit.amazonaws.com <br/>
codedeploy.${aws::region}.amazonaws.com <br/>
codedeploy.amazonaws.com <br/>
codeguru-reviewer.amazonaws.com <br/>
codepipeline.amazonaws.com <br/>
codestar-notifications.amazonaws.com <br/>
codestar.amazonaws.com <br/>
cognito-identity.amazonaws.com <br/>
cognito-idp.amazonaws.com <br/>
cognito-sync.amazonaws.com <br/>
comprehend.amazonaws.com <br/>
config-conforms.amazonaws.com <br/>
config-multiaccountsetup.amazonaws.com <br/>
config.amazonaws.com <br/>
connect.amazonaws.com <br/>
continuousexport.discovery.amazonaws.com <br/>
costalerts.amazonaws.com <br/>
custom-resource.application-autoscaling.amazonaws.com <br/>
databrew.amazonaws.com <br/>
datapipeline.amazonaws.com <br/>
datasync.amazonaws.com <br/>
dax.amazonaws.com <br/>
deeplens.amazonaws.com <br/>
delivery.logs.amazonaws.com <br/>
diode.amazonaws.com <br/>
directconnect.amazonaws.com <br/>
discovery.amazonaws.com <br/>
dlm.amazonaws.com <br/>
dms.amazonaws.com <br/>
ds.amazonaws.com <br/>
dynamodb.amazonaws.com <br/>
dynamodb.application-autoscaling.amazonaws.com <br/>
ec.amazonaws.com <br/>
ec2.amazonaws.com <br/>
ec2.application-autoscaling.amazonaws.com <br/>
ec2fleet.amazonaws.com <br/>
ec2scheduled.amazonaws.com <br/>
ecr.amazonaws.com <br/>
ecs-tasks.amazonaws.com <br/>
ecs.amazonaws.com <br/>
ecs.application-autoscaling.amazonaws.com <br/>
edgelambda.amazonaws.com <br/>
eks-fargate-pods.amazonaws.com <br/>
eks-fargate.amazonaws.com <br/>
eks-nodegroup.amazonaws.com <br/>
eks.amazonaws.com <br/>
elasticache.amazonaws.com <br/>
elasticbeanstalk.amazonaws.com <br/>
elasticfilesystem.amazonaws.com <br/>
elasticloadbalancing.amazonaws.com <br/>
elasticmapreduce.amazonaws.com <br/>
elastictranscoder.amazonaws.com <br/>
email.cognito-idp.amazonaws.com <br/>
emr-containers.amazonaws.com <br/>
es.amazonaws.com <br/>
events.amazonaws.com <br/>
firehose.amazonaws.com <br/>
fms.amazonaws.com <br/>
forecast.amazonaws.com <br/>
freertos.amazonaws.com <br/>
fsx.amazonaws.com <br/>
galaxy.amazonaws.com <br/>
gamelift.amazonaws.com <br/>
glacier.amazonaws.com <br/>
globalaccelerator.amazonaws.com <br/>
glue.amazonaws.com <br/>
greengrass.amazonaws.com <br/>
guardduty.amazonaws.com <br/>
health.amazonaws.com <br/>
honeycode.amazonaws.com <br/>
iam.amazonaws.com <br/>
imagebuilder.amazonaws.com <br/>
importexport.amazonaws.com <br/>
inspector.amazonaws.com <br/>
iot.amazonaws.com <br/>
iotanalytics.amazonaws.com <br/>
iotevents.amazonaws.com <br/>
iotsitewise.amazonaws.com <br/>
iotthingsgraph.amazonaws.com <br/>
ivs.amazonaws.com <br/>
jellyfish.amazonaws.com <br/>
kafka.amazonaws.com <br/>
kinesis.amazonaws.com <br/>
kinesis.{us-gov-region}.amazonaws.com <br/>
kinesisanalytics.amazonaws.com <br/>
kms.amazonaws.com <br/>
lakeformation.amazonaws.com <br/>
lambda.amazonaws.com <br/>
lex.amazonaws.com <br/>
license-manager.amazonaws.com <br/>
lightsail.amazonaws.com <br/>
logger.cloudfront.amazonaws.com <br/>
logs.amazonaws.com <br/>
machinelearning.amazonaws.com <br/>
macie.amazonaws.com <br/>
managedblockchain.amazonaws.com <br/>
managedservices.amazonaws.com <br/>
mediaconnect.amazonaws.com <br/>
mediaconvert.amazonaws.com <br/>
mediapackage.amazonaws.com <br/>
mediastore.amazonaws.com <br/>
mediatailor.amazonaws.com <br/>
member.org.stacksets.cloudformation.amazonaws.com <br/>
metering-marketplace.amazonaws.com <br/>
mgn.amazonaws.com <br/>
migrationhub.amazonaws.com <br/>
mobileanalytics.amazonaws.com <br/>
mobilehub.amazonaws.com <br/>
monitoring.amazonaws.com <br/>
monitoring.rds.amazonaws.com <br/>
mq.amazonaws.com <br/>
network-firewall.amazonaws.com <br/>
ops.apigateway.amazonaws.com <br/>
opsworks-cm.amazonaws.com <br/>
opsworks.amazonaws.com <br/>
organizations.amazonaws.com <br/>
personalize.amazonaws.com <br/>
pinpoint.amazonaws.com <br/>
polly.amazonaws.com <br/>
purchaseorders.amazonaws.com <br/>
qldb.amazonaws.com <br/>
quicksight.amazonaws.com <br/>
ram.amazonaws.com <br/>
rds-preview.amazonaws.com <br/>
rds.amazonaws.com <br/>
redshift.amazonaws.com <br/>
rekognition.amazonaws.com <br/>
replication.dynamodb.amazonaws.com <br/>
replicator.lambda.amazonaws.com <br/>
resource-groups.amazonaws.com <br/>
robomaker.amazonaws.com <br/>
route53.amazonaws.com <br/>
route53domains.amazonaws.com <br/>
route53resolver.amazonaws.com <br/>
s3.amazonaws.com <br/>
sagemaker.amazonaws.com <br/>
secretsmanager.amazonaws.com <br/>
securityhub.amazonaws.com <br/>
serverlessrepo.amazonaws.com <br/>
servicecatalog-appregistry.amazonaws.com <br/>
servicecatalog.amazonaws.com <br/>
servicediscovery.amazonaws.com <br/>
ses.amazonaws.com <br/>
shield.amazonaws.com <br/>
signer.amazonaws.com <br/>
signin.amazonaws.com <br/>
sms.amazonaws.com <br/>
sns.amazonaws.com <br/>
spotfleet.amazonaws.com <br/>
sqs.amazonaws.com <br/>
ssm-incidents.amazonaws.com <br/>
ssm.amazonaws.com <br/>
sso.amazonaws.com <br/>
states.amazonaws.com <br/>
storagegateway.amazonaws.com <br/>
streams.metrics.cloudwatch.amazonaws.com <br/>
sts.amazonaws.com <br/>
support.amazonaws.com <br/>
swf.amazonaws.com <br/>
tagging.amazonaws.com <br/>
tagpolicies.tag.amazonaws.com <br/>
textract.amazonaws.com <br/>
timestream.amazonaws.com <br/>
transcribe.amazonaws.com <br/>
transfer.amazonaws.com <br/>
transitgateway.amazonaws.com <br/>
translate.amazonaws.com <br/>
trustedadvisor.amazonaws.com <br/>
tts.amazonaws.com <br/>
vmie.amazonaws.com <br/>
vpc-flow-logs.amazonaws.com <br/>
waf-regional.amazonaws.com <br/>
waf.amazonaws.com <br/>
wam.amazonaws.com <br/>
workdocs.amazonaws.com <br/>
worklink.amazonaws.com <br/>
workmail.amazonaws.com <br/>
workspaces.amazonaws.com <br/>
xray.amazonaws.com <br/>
{region}.elasticache-snapshot.amazonaws.com <br/>