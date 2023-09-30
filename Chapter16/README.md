# Chapter 16 - Building a Modern Data Platform on AWS

In this chapter we reviewed high-level concepts around building a modern data platform on AWS. 
We covered some of the puzzle pieces that need to be in place in order to build a data platform that is flexible and agile, scalable, 
well goverened, and secure, while also being easy to use and enable data producers and consumers to self-serve.

We examined the pros and cons of building or buying a data platform, and then looked at how a DataOps approach to the development
of a platform helps enable automation and observability. We examined how tools such as CloudFormation can be used to automate and manage
the process of deploying data infrastructure, and how we can use Source Control Systems to manage our code for data transformation (such
as PySpark jobs that we run in AWS Glue). 

We then examined a number of tools that enable a DataOps approach, including CloudFormation, CodeCommit, CodeBuild and CodePipeline. 

## Hands-on Activity
In the hands-on activity for this chapter, we set up a CodeCommit repository, and then added Glue ETL code and a CloudFormation template 
to the repository using Git. We then built two pipelines using CodePipeline - one to write out Glue ETL code to S3 whenever the file is updated in 
CodeCommit, and a second one to deploy our CloudFormation template, whenever the template is updated. 

#### Setting up a Cloud9 IDE environment

- AWS Management Console - Cloud9: https://us-east-2.console.aws.amazon.com/cloud9control/home

- Commands to configure a Git username and password. Change the example below to reflect your name and email address.
```
git config --global user.name "Gareth Eagar"
git config --global user.email gareth.eagar@example.com
```

- Configuring the AWS CLI credential helper to automate provisioning of credentials needed to authenticate to CodeCommit
```
git config --global credential.helper '!aws codecommit credential-helper $@'
git config --global credential.UseHttpPath true
```

- Creating a directory for your Git repository
```
cd /home/ec2-user/environment
mkdir git
cd git
```

#### Setting up our AWS CodeCommit repository

- AWS Management Console - CodeCommit: https://us-east-2.console.aws.amazon.com/codesuite/codecommit/repositories

- Use the HTTPS link under Clone URL to copy the link to clone your repository. Then run `git clone <paste_the_link>`. For example:
```
git clone https://git-codecommit.us-east-2.amazonaws.com/v1/repos/data-product-film
```

- Create new directories in the repository, using the Cloud9 terminal window
```
cd data-product-film
mkdir glueETL_code
mkdir cfn_templates
```

- Create a new Amazon S3 bucket to store the resources for our film data product.
```
aws s3 mb s3://data-product-film-initials
```

#### Adding a Glue ETL script and CloudFormation template into our repository

- Access the [Glue-streaming_views_by_category.py](/Chapter16/Glue-streaming_views_by_category.py) file in this repository, and paste it into a new file in your Cloud9 IDE environment.

  **Make sure to change the S3 bucket path on Line 47 of the code to match the name of your curated zone bucket**

- Access the [CFN-glue_job-streams_by_category.cfn](/Chapter16/CFN-glue_job-streams_by_category.cfn) file in this repository, and paste it into a new file in your Cloud9 IDE environment.

  **Make sure to change the S3 bucket path on Line 22 of the template to match the name of the bucket you created earlier in this exercise**

- Commit the newly created files into your repository by running the following commands in the Cloud9 terminal
```
git add .
git commit -m "Initial commit of CloudFormation template and Glue code for our streaming views by category data product"
git push
```

- Access the [CodeCommit](https://us-east-1.console.aws.amazon.com/codesuite/codecommit/repositories) service in the AWS Management Console, and ensure that the two files have been written to your repository

#### Automating deployment of our Glue code

- AWS Management Console - CodePipeline: https://us-east-1.console.aws.amazon.com/codesuite/codepipeline/pipelines

#### Automating deployment of our Glue job

- AWS Management Console - IAM: https://us-east-1.console.aws.amazon.com/iamv2/home

- Edit the `DataEngGlueCWS3CuratedZoneRole`, and replace the current **Trust relationship** JSON with the JSON in [DataEngGlueCWS3CuratedZoneRole-trust-policy.json](/Chapter16/DataEngGlueCWS3CuratedZoneRole-trust-policy.json) in this repository

- In the permissions tab for the role, edit the DataEngGlueCWS3CuratedZoneWrite role to add in S3 permissions for the new bucket you created earlier. The new S3 permissions should look as follows (but reflect the name of your buckets):
```
{
            "Effect": "Allow",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                "arn:aws:s3:::dataeng-landing-zone-gse23/*",
                "arn:aws:s3:::dataeng-clean-zone-gse23/*",
                "arn:aws:s3:::data-product-film-gse23/*"
            ]
        }
```








