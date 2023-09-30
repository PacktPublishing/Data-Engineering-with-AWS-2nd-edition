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

#### Setting up our AWS CodeCommit repositories

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

- Access the Glue-streaming_views_by_category.py file in this repository, and paste it into a new file in your Cloud9 IDE environment.

