# Chapter 13 - Enabling Artificial Intelligence and Machine Learning

In this chapter, you learned more about the broad range of AWS ML and AI services,
and had the opportunity to get hands-on with Amazon Comprehend, an AI service for
extracting insights from written text.  

We discussed how ML and AI services can apply to a broad range of use cases, both
specialized (such as detecting cancer early) and general (business forecasting or
personalization).  

We examined different AWS services related to ML and AI. We looked at how different
Amazon SageMaker capabilities can be used to prepare data for ML, build models, train
and fine-tune models, and deploy and manage models. SageMaker makes building custom
ML models much more accessible to developers without existing expertise in ML.  

We then looked at a range of AWS AI services that provide prebuilt and trained models for
common use cases. We looked at services for transcribing text from audio files (Amazon
Transcribe), for extracting text from forms and handwritten documents (Amazon
Textract), for recognizing images (Amazon Rekognition), and for extracting insights from
text (Amazon Comprehend). We also briefly discussed other business-focused AI services,
such as Amazon Forecast and Amazon Personalize.

Finally, we did a quick overview of what Generative AI, Foundation Models, and Large Language
Models are, and examined how Generative AI solutiosn can be built on AWS. 

## Useful links
The links below cover some of the services that were overviewed in this chapter.

### SageMaker Components
- [Amazon SageMaker](https://aws.amazon.com/sagemaker/)
- [Amazon SageMaker Ground Truth](https://aws.amazon.com/sagemaker/data-labeling/)
- [Amazon SageMaker Data Wrangler](https://aws.amazon.com/sagemaker/data-wrangler)
- [Amazon SageMaker Clarify](https://aws.amazon.com/sagemaker/clarify)
- [Amazon SageMaker Notebooks](https://aws.amazon.com/sagemaker/notebooks/)
- [Amazon SageMaker Autopilot](https://aws.amazon.com/sagemaker/autopilot)
- [Amazon SageMaker JumpStart](https://aws.amazon.com/sagemaker/jumpstart)
- [Amazon SageMaker Experiments](https://aws.amazon.com/sagemaker/experiments/)
- [Amazon SageMaker Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/)

### AWS Serivces for AI
- [Amazon Transcribe](https://aws.amazon.com/transcribe/)
- [Amazon Textract](https://aws.amazon.com/textract/)
- [Amazon Comprehend](https://aws.amazon.com/comprehend/)
- [Amazon Rekognition](https://aws.amazon.com/rekognition/)
- [Amazon Forecast](https://aws.amazon.com/forecast/)
- [Amazon Fraud Detector](https://aws.amazon.com/fraud-detector/)
- [Amazon Personalize](https://aws.amazon.com/personalize/)

### AWS Services for Generative AI
- [Blog post - Get started with generative AI on AWS using Amazon SageMaker JumpStart](https://aws.amazon.com/blogs/machine-learning/get-started-with-generative-ai-on-aws-using-amazon-sagemaker-jumpstart/)
- [Amazon Bedrock](https://aws.amazon.com/bedrock/)
- [Amazon Titan](https://aws.amazon.com/bedrock/titan/)

## Hands-on Activity
In the hands-on acitvity section of this chapter we looked at how we can use the 
[Amazon Comprehend](https://aws.amazon.com/comprehend/) service to gain insight into the sentiment 
of reviews posted to a website. We configured an SQS queue to receive the details 
of newly posted reviewes, and had a Lambda function configured to pass the review text to Amazon 
Comprehend to gain insight into the review sentiment (postivie, negative, or netural). 

#### Setting up a new Amazon SQS message queue

- Amazon Management Console - SQS: https://console.aws.amazon.com/sqs/v2/.

#### Creating a Lambda function for calling Amazon Comprehend

- Amazon Management Console - Lambda: https://console.aws.amazon.com/lambda/

- Lambda function code for calling Amazon Comprehend for sentiment analysis: [website-reviews-analysis-role.py](website-reviews-analysis-role.py)  

  **[ Make sure to set region on Line 4 to the correct region that you are using for the hands-on activities in this book ]**

#### Testing the solution with Amazon Comprehend

- Example of a postivie review

```
I recently stayed at the Kensington Hotel in downtown Cape Town and was very impressed. 
The hotel is beautiful, the service from the staff is amazing, and the sea views cannot be beaten. 
If you have the time, stop by Elizabeth's Kitchen, a coffee shop not far from the hotel, 
to get a coffee and try some of their delicious cakes and baked goods.
```






