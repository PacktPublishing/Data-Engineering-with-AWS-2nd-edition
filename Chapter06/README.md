# Chapter 6 - Ingesting Batch and Streaming Data

In this chapter, we discussed the 5 V's of data (volume, velocity, variety, validity, and value). 
We then reviewed a few different approaches for ignesting data from databases, and from streaming data sources.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter, we deployed an **Amazon CloudFormation** template that provisioned an **Amazon RDS MySQL** database instance, as well as an **Amazon EC2** instance, which was used to load a demo database into the MySQL database instance. We then configured **Amazon Database Migration Service (DMS)** to ingest data from the MySQL database, and then we configured **Amazon Kinesis Data Firehose** to ingest streaming data that we generated using the **Amazon Kinesis Data Generator (KDG)**.

### Deploying MySQL and an EC2 data loader via AWS CloudFormation
- Download the CloudFormation template from [here](./mysql-ec2loader.cfn)

- AWS Management Console - CloudFormation: https://us-east-2.console.aws.amazon.com/cloudformation

- CloudFormation Stack Name: `dataeng-aws-chapter6-mysql-ec2`

#### Creating an IAM policy and role for DMS

- AWS Management Console - IAM Policies: https://console.aws.amazon.com/iamv2/home?#/policies

- AWS IAM policy for `DataEngDMSLandingS3BucketPolicy`. **Change INITIALS in the policy below to match the name of the landing zone bucket that you previously created**. 
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:*"
            ],
            "Resource": [
                "arn:aws:s3:::dataeng-landing-zone-INITIALS",
                "arn:aws:s3:::dataeng-landing-zone-INITIALS/*"
            ]
        }
    ]
}
```
- IAM Policy Name: `DataEngDMSLandingS3BucketPolicy`
- IAM Role Name: `DataEngDMSLandingS3BucketRole`

#### Configuring DMS settings and performing a full load from MySQL to S3
- Replication instance name: `mysql-s3-replication`
- Target endpoint identifier: `s3-landing-zone-sakilia-csv`
- Migration task identifier: `dataeng-mysql-s3-sakila-task`
- Schema Source Name: `%sakila%`

#### Querying data with Amazon Athena
- Athena S3 Query Bucket Name: `athena-query-results-<INITIALS>`. **Change \<INITIALS\> to the unique identifier you have been using for bucket names**.

- Athena query to validate that data has been successfully ingested using DMS  
`select * from film limit 20;`

- Further reading: [Using Amazon S3 as a target for AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Target.S3.html)

- Further reading: [Using a MySQL-compatible database as a source for AWS DMS](https://docs.aws.amazon.com/dms/latest/userguide/CHAP_Source.MySQL.html)

### Ingesting Streaming Data

#### Configuring Kinesis Data Firehose for streaming delivery to Amazon S3
- AWS Management Console - Kinesis Firehose: https://us-east-2.console.aws.amazon.com/firehose/home
- Kinesis Firehose Delivery Stram Name: `dataeng-firehose-streaming-s3`
- *S3 Bucket Prefix* for Kinesis Data Firehose: `streaming/!{timestamp:yyyy/MM/}`
- *S3 Bucket Error Output Prefix* for Kinesis Data Firehose: `!{firehose:error-output-type}/!{timestamp:yyyy/MM/}`

#### Configuring Amazon Kinesis Data Generator (KDG)
- Kinesis Data Generator Help Page: https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html
- Documentation for mapping region names to region ID's: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Concepts.RegionsAndAvailabilityZones.html
- Record template for Kinesis Data Generator
```
{
    "timestamp":"{{date.now}}",
    "eventType":"{{random.weightedArrayElement(
        {
            "weights": [0.3,0.1,0.6],
            "data": ["rent","buy","trailer"]
        }
    )}}",
    "film_id":{{random.number(
    {
        "min":1,
        "max":1000
    }
    )}},
    "distributor":"{{random.arrayElement(
        ["amazon prime", "google play", "apple itunes","vudo", "fandango now", "microsoft", "youtube"]
    )}}",
    "platform":"{{random.arrayElement(
        ["ios", "android", "xbox", "playstation", "smarttv", "other"]
    )}}",
    "state":"{{address.state}}"
}
```

#### Querying data with Amazon Athena
- AWS Management Console - Glue: https://us-east-2.console.aws.amazon.com/glue/home
- Crawler name: `dataeng-streaming-crawler`
- Crawler S3 data path: s3://dataeng-landing-zone-<initials>/streaming/
- Athena query to validate that data has been successfully ingested using DMS:   
`select * from streaming limit 20;`



