# Chapter 2 - Data Management Architectures for Analytics
In this chapter, we learned about the foundational architectural concepts that are typically applied when designing real-life analytics data management and processing solutions. 
We also did a deep-dive into three analytics data management architectures that are popular today: data warehouses, data lakes, and data lakehouses.

## Hands-on Activity
In the ***hands-on activity*** section, you learnt how to access the AWS Command Line Interface (CLI) via AWS CloudShell, and then used the CLI to create Amazon S3 buckets (storage containers in the Amazon S3 service) which we will use in later chapters. 

### Links
- **Learn more about S3 bucket naming rules:** https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html
- **AWS CloudShell service:** https://us-east-2.console.aws.amazon.com/cloudshell/home

### Commands
#### Create a new Amazon S3 bucket
The following command, when run via the AWS CLI, creates a new bucket called *dataeng-test-bucket-123*. If a bucket with this name already exists the command will fail, so you need to ensure you provide a globally unique name.  

```
aws s3 mb s3://dataeng-test-bucket-123
```
