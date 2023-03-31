# Chapter 3 - The AWS Data Engineers Toolkit
In this chapter we reviewed a range of AWS services at a high level, including services for ingesting data from a variety of sources, services for transforming data, services for orchestrating pipelines, and services for consuming and working with data.

## Hands-on Activity
In the ***hands-on activity*** section of this chapter, we configured an S3 bucket to automatically trigger a Lambda function whenever a new CSV file was written to the bucket. In the Lambda function, we used an open-source library to convert the CSV file into Parquet format, and wrote the file out to a new zone of our data lake.

#### Creating a Lambda layer containing the AWS SDK for Pandas (awswrangler) library
- AWS SDK for Pandas site: https://github.com/aws/aws-sdk-pandas
- AWS Data Wrangler v2.19 ZIP file for Python 3.9: https://github.com/aws/aws-sdk-pandas/releases/download/2.19.0/awswrangler-layer-2.19.0-py3.9.zip
- AWS Management Console - Lambda Layers: https://console.aws.amazon.com/lambda/home#/layers

#### Creating an IAM policy and role for your Lambda function
- AWS Management Console - IAM Policies: https://console.aws.amazon.com/iamv2/home?#/policies
- Policy JSON for `DataEngLambdaS3CWGluePolicy`: [DataEngLambdaS3CWGluePolicy](DataEngLambdaS3CWGluePolicy.json)  
  [Ensure you replace INITIALS in the policy statements to reflect the name of the S3 buckets you created]

#### Creating a Lambda function
- AWS Management Console - Lambda Functions: https://console.aws.amazon.com/lambda/home#/functions
- `CSVtoParquetLambda` function code: [CSVtoParquetLambda.py](CSVtoParquetLambda.py)  
 **Note:** Make sure you don't miss the step about increasing the Lambda function timeout to 1 minute. If using a larger CSV file than the file provided here as a sample (test.csv) then consider also increasing the memory allocation. 

#### Configuring our Lambda function to be triggered by an S3 upload
- Sample CSV file: [test.csv](test.csv)

#### Command to list the newly created Parquet files in the clean-zone bucket: 
###### Ensure you replace INITIALS below to reflect the name of the bucket you previously created

```
aws s3 ls s3://dataeng-clean-zone-INITIALS/cleanzonedb/csvtoparquet/
```
  
