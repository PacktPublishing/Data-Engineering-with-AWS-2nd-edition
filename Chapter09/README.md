# Chapter 9 - A deeper-dive into Data Marts and Amazon Redshift

In this chapter, we learned how a cloud data warehouse can be used to
optimize performance for hot data. We reviewed some common "anti-patterns"
for data warehouse usage before diving deep into Redshift architecture to learn more
about how Redshift optimizes data storage across nodes.

We then reviewed some of the important design decisions that need to be made when
creating a Redshift cluster in order to optimize performance while balancing costs, and also
reviewed ssome of the advanced Redshift features. 

## Hands-on Activity
In the hands-on section of this chapter we created a new Redshift Serverless cluster,
configured Redshift Spectrum to query data from Amazon S3, and then loaded a
subset of data from S3 into Redshift. 

### Uploading our sample data to Amazon S3
In this exercise, we use some fake data that was created using a tool called [Mockaroo](https://www.mockaroo.com/). 

Download our fake user data with the following link: [user_details.csv](user_details.csv). When you open the link, click on the three dots, and then click on `Download`.

Open the Amazon S3 console with the following link: https://s3.console.aws.amazon.com/s3

#### IAM Roles for Redshift

- AWS Management Console - IAM Roles: https://console.aws.amazon.com/iamv2/home?#/roles

#### Creating a Redshift cluster

- AWS Management Console - Redshift: https://console.aws.amazon.com/redshiftv2/

#### Using Redshift Spectrum to directly query data in the data lake

- The following query can be run in the Redshift Query Editor to create an external schema. Make sure to specify the ARN for the new role you created in place of the ***iam_role*** listed below.

```
create external schema spectrum_schema
from data catalog
database 'users'
iam_role 'arn:aws:iam::1234567890:role/AmazonRedshiftSpectrumRole'
create external database if not exists;
```

- The following query can be run to create a new external table. Make sure to replace ***INITIALS*** in the query below with the correct identifier for your Landing Zone bucket.

```
CREATE EXTERNAL TABLE spectrum_schema.user_details(
  id INTEGER,
  first_name VARCHAR(40),
  last_name VARCHAR(40),
  email VARCHAR(60),
  gender VARCHAR(15),
  address_1 VARCHAR(80),
  address_2 VARCHAR(80),
  city VARCHAR(40),
  state VARCHAR(25),
  zip VARCHAR(5),
  phone VARCHAR(12)
)
row format delimited
fields terminated by ','
stored as textfile
location 's3://dataeng-landing-zone-initials/users/'
table properties ('skip.header.line.count'='1');
```

**Query 1:**  
```
select * from spectrum_schema.user_details limit 10;
```









