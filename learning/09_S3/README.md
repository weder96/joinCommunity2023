# S3

## CLI

### **Create S3 Bucket**

```
aws s3 mb s3://s3-join-community-2023-files
```

### **Create S3 bucket in specific AWS region**

```
aws s3 mb s3://s3-join-community-2023-files-us-ea-2 --region us-east-2
```

### **put version at bucket**

```
aws s3api put-bucket-versioning --bucket s3-join-community-2023-files-us-ea-2  --versioning-configuration Status=Enabled
```

### **check bucket status version**
```
aws s3api get-bucket-versioning --bucket s3-join-community-2023-files-us-ea-2
```

### **Suspending versioning**
```
aws s3api put-bucket-versioning --bucket  s3-join-community-2023-files-us-ea-2 --versioning-configuration Status=Suspended
```


### **Copy files to S3 bucket**
```
aws s3 cp images/ s3://s3-join-community-2023-files --recursive --include "*.jpg"
```

### **List S3 buckets**

```
aws s3 ls
```

```
aws s3 ls s3://s3-join-community-2023-files --recursive
```

```
aws s3 ls s3://
```

aws s3 ls s3://s3-join-community-2023-files  --recursive  --human-readable --summarize

### **The aws s3api list-buckets command produces JSON as an output:**

### List S3 buckets (JSON output)
```
aws s3api list-buckets
```

### Download a File from S3 Bucket

**Follow the instructions below to retrieve a specific file from an S3 bucket. The next command transfers getdata.php from the specified S3 bucket to the current directory:**

```
aws s3 cp s3://s3-join-community-2023-files/rabisco.png .
```

**As seen below, you can download the file to your local computer with various names:**
**As seen below, you can download the file to your local computer with a different name:**
```
aws s3 cp s3://s3-join-community-2023-files/rabisco.png rabisco_new.png
```


**Download the file from the S3 bucket to the designated local computer folder as seen below. This will download the rabisco.png file to the local machine’s ./img/project/ folder:**
```
aws s3 cp s3://s3-join-community-2023-files/rabisco.png ./img/project/
```

### Move a File from Local to S3 Bucket
**As you may anticipate, when you transfer a file from a local system to an S3 bucket, the file is really transported from the local machine to the S3 bucket:**

```
aws s3 mv ./file/hello.json s3://s3-join-community-2023-files
```


### Move All Files from a Local Folder to S3 Bucket
**The following files are located in the subdirectory in this example:**
```
 ls -1 ./file

 aws s3 mv ./file s3://s3-join-community-2023-files/file --recursive

```


### Filter S3 bucket list results (JSON output)
```
aws s3api list-buckets --query \
  'Buckets[?starts_with(Name, `s3-join`) == `true`].Name'
```

### Filter S3 bucket list results (text output)
```
aws s3api list-buckets --query \
  'Buckets[?starts_with(Name, `s3-join`) == `true`].[Name]' \
  --output text
```

### Delete empty S3 bucket
```
aws s3 rb s3://s3-join-community-2023-files-us-ea-2
```

### Delete non-empty S3 bucket
```
aws s3 rb s3://s3-join-community-2023-files-us-ea-2 --force
```

### Deleting S3 bucket with enabled versioning
```
export bucket_name="hands-on-cloud-versioning-enabled"
```

### Deleting objects versions
```
aws s3api delete-objects \
    --bucket s3-join-community-2023-files-us-ea-2 \
    --delete "$(aws s3api list-object-versions \
    --bucket s3-join-community-2023-files-us-ea-2 \
    --output=json \
    --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
```

```
aws s3api delete-objects \
    --bucket $bucket_name \
    --delete "$(aws s3api list-object-versions \
    --bucket $bucket_name \
    --output=json \
    --query='{Objects: Versions[].{Key:Key,VersionId:VersionId}}')"
```

### Deleting delete markers
```
aws s3api delete-objects \
    --bucket $bucket_name \
    --delete "$(aws s3api list-object-versions \
    --bucket $bucket_name \
    --output=json \
    --query='{Objects: Contents[].{Key:Key,VersionId:VersionId}}')"
```

### **Deleting S3 bucket**
```
aws s3 rb s3://s3://s3-join-community-2023-files-us-ea-2
```

### Upload file to S3 bucket

```
aws s3 cp ./images/5b124202-1098-4822-b39a-c2dc6e93704c.jpeg s3://s3-join-community-2023-files-us-ea-2
```

### If required, you can change the uploaded S3 object name during the upload operation:

```
aws s3 cp ./images/5b124202-1098-4822-b39a-c2dc6e93704c.jpeg s3://s3-join-community-2023-files-us-ea-2/image.png
```



### Resources
https://docs.aws.amazon.com/cli/latest/reference/s3/

https://hands-on.cloud/aws-cli-s3-examples/

https://hands-on.cloud/amazon-s3/

https://intellipaat.com/blog/aws-s3-cli-commands/

https://www.learnaws.org/2022/08/21/enable-disable-s3-versioning/


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