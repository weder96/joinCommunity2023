# Dynamodb

## CLI

### **Create table DynamoBD**

```
aws dynamodb create-table \
    --table-name Order \
    --attribute-definitions \
        AttributeName=id,AttributeType=S \
        AttributeName=status,AttributeType=S \
    --key-schema \
        AttributeName=id,KeyType=HASH \
        AttributeName=status,KeyType=RANGE \
    --provisioned-throughput \
        ReadCapacityUnits=5,WriteCapacityUnits=5 \
    --table-class STANDARD
```

### **Describe table DynamoBD**

```
aws dynamodb describe-table --table-name Order
```


### **Put Item DynamoBD** 

```
aws dynamodb put-item \
    --table-name Order  \
    --item \
        '{"id": {"S": "1"}, "status": {"S": "IN_PROGRESS"}, "desc": {"S": "Xiomi readmi 11 order"}, "orderDate": {"S": "2023-08-10"}}'

aws dynamodb put-item \
    --table-name Order  \
    --item \
        '{"id": {"S": "4"}, "status": {"S": "DELIVERY"}, "desc": {"S": "Xiomi readmi 12 order"}, "orderDate": {"S": "2023-08-10"}}'
```


### **Read Data into DynamoDB Table with AWS CLI**
---

```
aws dynamodb get-item --consistent-read \
    --table-name Order \
    --key '{ "id": {"S": "4"}, "status": {"S": "DELIVERY"}}'
```


### **Update Data into DynamoDB Table with AWS CLI**
---

```
aws dynamodb update-item \
    --table-name Order \
    --key '{ "id": {"S": "1"}, "status": {"S": "DELIVERY"}}' \
    --update-expression "SET orderDate = :newval" \
    --expression-attribute-values '{":newval":{"S":"2023-08-14"}}' \
    --return-values ALL_NEW
```

### **Query Data into DynamoDB Table with AWS CLI**
---

```
aws dynamodb query \
    --table-name Order \
    --key-condition-expression "id = :id" \
    --expression-attribute-values  '{ ":id":{"S":"1"}}'
```


### **CRUD Operations into DynamoDB Table with AWS CLI**
---

### Create an item
**Create an item in the Order table using the INSERT PartiQL statement.**
```
aws dynamodb execute-statement --statement "INSERT INTO \"Order\" VALUE {'id':'2','status':'IN_PROGRESS'}"
```

---
### Retrieve an item 
**Retrieve an item from the Order table using the SELECT PartiQL statement.**

```
aws dynamodb execute-statement --statement "SELECT * FROM \"Order\" WHERE id='2' AND status='IN_PROGRESS'"
```

---
### Update an item
**Update an item in the Order table using the UPDATE PartiQL statement.**

```
aws dynamodb execute-statement --statement "UPDATE \"Order\"  SET description='updated order' WHERE id='2' AND status='IN_PROGRESS'"
```


---
### Delete an item
**Delete an item from the Order table using the DELETE PartiQL statement.**

```
aws dynamodb execute-statement --statement "DELETE  FROM \"Order\" WHERE id='2' AND status='IN_PROGRESS'"
```

---
### Delete Table:
```
aws dynamodb delete-table --table-name Order
```

### Resources

https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_CreateTable.html

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/getting-started-step-2.html

https://docs.aws.amazon.com/pt_br/lambda/latest/dg/with-ddb-example.html

https://medium.com/aws-lambda-serverless-developer-guide-with-hands/dynamodb-streams-using-aws-lambda-to-process-dynamodb-streams-for-change-data-capture-2e3ab8df27ca


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