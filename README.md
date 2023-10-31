# Data Engineering with AWS, Second Edition
This is the code repository for [Data Engineering with AWS, Second Edition](https://www.packtpub.com/product/data-engineering-with-aws-second-edition/9781804614426), published by Packt.   
**Acquire the skills to design and build AWS-based data transformation pipelines like a pro**

The author of this book is -[Gareth Eagar](https://www.linkedin.com/in/garetheagar/)
## About the book

This book, authored by a seasoned Senior Data Architect with 25 years of experience, aims to help you achieve proficiency in using the AWS ecosystem for data engineering. This revised edition provides updates in every chapter to cover the latest AWS services and features, takes a refreshed look at data governance, and includes a brand-new section on building modern data platforms which covers; implementing a data mesh approach, open-table formats (such as Apache Iceberg), and using DataOps for automation and observability.

You'll begin by reviewing the key concepts and essential AWS tools in a data engineer's toolkit and by getting acquainted with modern data management approaches. You'll then architect a data pipeline, review raw data sources, transform the data, and learn how that transformed data is used by various data consumers. You’ll learn how to ensure strong data governance, and about populating data marts and data warehouses along with how a data lakehouse fits into the picture. After that, you'll be introduced to AWS tools for analyzing data, including those for ad-hoc SQL queries and creating visualizations. Then, you'll explore how the power of machine learning and artificial intelligence can be used to draw new insights from data. In the final chapters, you'll discover transactional data lakes, data meshes, and how to build a cutting-edge data platform on AWS.

By the end of this AWS book, you'll be able to execute data engineering tasks and implement a data pipeline on AWS like a pro!

## Key Takeaways
- Delve into robust AWS tools for ingesting, transforming, and consuming data, and for orchestrating pipelines
- Stay up to date with a comprehensive revised chapter on Data Governance
- Build modern data platforms with a new section covering transactional data lakes and data mesh



## New Edition v/s Previous Edition: 
- New and refreshed content.
- Fully revised with the most up-to-date information on AWS.




## What's New 
- Updates to every single chapter to cover all the newest AWS services and features.
- Three brand-new chapters, including content on building transactional data lakes, implementing a data mesh approach on AWS, and using a DataOps approach to data platform building.
- Modernized coverage of AI and ML functionality within AWS.
- A new and refreshed look at data governance strategies.





## Outline and Chapter Summary
This new edition builds on the work of the original to bring you a fully refreshed, definitive guide to building data pipelines in AWS. You’ll move from the basics of learning what data engineering is and what goes into designing strong architectures, to exploring the tools and services available to help you and how to get the most out of them, before covering recent developments in the data engineering space, like transactional data lakes, AI, and ML.
Throughout the book you’ll cement your newfound knowledge with a series of easy to follow practical exercises.

1. [An Introduction to Data Engineering](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter01)
2. [Data Management Architectures for Analytics](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter02)
3. [The AWS Data Engineers Toolkit](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter03)
4. [Data Cataloging, Security, and Governance](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter04)
5. [Architecting Data Engineering Pipelines](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter05)
6. [Ingesting Batch and Streaming Data](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter06)
7. [Transforming Data to Optimize for Analytics](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter07)
8. [Identifying and Enabling Data Consumers](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter08)
9. [Loading Data into a Dart Mart](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter09)
10. [Orchestrating the Data Pipeline](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter10)
11. [Ad Hoc Queries with Amazon Athena](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter11)
12. [Visualizing Data with Amazon QuickSight](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter12)
13. [Enabling Artificial Intelligence and Machine Learning](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter13)
14. [Transactional Data Lakes](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter14)
15. [Implementing a Data Mesh strategy](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter15)
16. [Building a modern data platform on AWS](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter16)
17. [Wrapping Up the First Part of Your Learning Journey](https://github.com/PacktPublishing/Data-Engineering-with-AWS-2nd-edition/tree/main/Chapter17)

### Chapter 01, An Introduction to Data Engineering
This chapter goes into the burgeoning field of data engineering, shedding light on its rapid growth and the soaring demand for professionals in this domain. With data assuming an increasingly pivotal role in organizations of all scales, the chapter underscores the gratification derived by individuals who relish assembling intricate data pipelines that not only ingest raw data, but also undertake its transformation and optimization for diverse consumer needs. It stresses the significance of data as a corporate asset, highlighting its escalating value, while concurrently examining the hurdles faced by organizations coping with surges in data volume. The chapter elucidates how data engineers can leverage cloud-based services to surmount these challenges, setting the stage for the practical activities presented later in the book. It also provides a comprehensive guide for creating a new Amazon Web Services (AWS) account.


**Key Insights**:
- Data engineering is a rapidly growing career path, with high demand being driven by the increasing importance of data in organizations.
- Data engineers play a critical role in building complex data pipelines that ingest, transform, and optimize raw data for various consumers.
- The chapter emphasizes the value of data as a corporate asset and discusses the challenges organizations face with growing data volumes.
- Cloud-based services are highlighted as a means for data engineers to address these challenges effectively.
- The chapter also introduces the foundational step of creating an Amazon Web Services (AWS) account, setting the stage for hands-on activities in later chapters.



### Chapter 02, Data Management Architectures for Analytics
This chapter underlines the diversity of options available in terms of cloud services, open-source frameworks, file formats, and architectural approaches for analytical projects, depending on specific business requirements. It serves as a foundational resource for understanding modern analytical architectures, regardless of whether one chooses to implement them on AWS or other platforms. The chapter provides essential introductory concepts that lay the groundwork for subsequent chapters, covering key topics such as the evolution of data management for analytics, in-depth exploration of data warehouse concepts and architecture, an overview of data lake architecture, and the synergy between data warehouses and data lakes. It also includes a practical component, guiding readers on using the AWS Command Line Interface (CLI) to create Simple Storage Service (S3) buckets.

Furthermore, the chapter emphasizes the importance of foundational architectural concepts in designing real-world analytics data management and processing solutions. It introduces three prevalent analytics data management architectures used in organizations today: data warehouses, data lakes, and data lakehouses.

**Key Insights**:

- Various cloud services, open-source frameworks, file formats, and architectural approaches can be employed in analytical projects, with choices dependent on specific business requirements.
- Foundational concepts and technologies essential for modern analytical architectures are discussed, irrespective of the cloud platform used, laying the groundwork for subsequent chapters.
- The chapter covers the evolution of data management for analytics, data warehouses, data lakes, and data lakehouses.
- Practical guidance is provided on using the AWS CLI to create S3 buckets.


### Chapter 03, The AWS Data Engineers Toolkit
This chapter highlights how cloud computing has transformed the traditional approach to big data processing. In the past, organizations grappled with the complexity of building and maintaining their own data processing systems, often leading to significant expenditures and delays. With AWS, many of these challenges have been eliminated, enabling the quick deployment of fully configured software solutions, automatic updates, and scalability without the need for large upfront capital investment. The chapter introduces a range of AWS-managed services used for building big data solutions, and emphasizes the importance of selecting the most suitable service for specific requirements.

The chapter provides a comprehensive overview of AWS services for data ingestion, data transformation, orchestrating big data pipelines, and data consumption. It also includes a hands-on component, guiding readers on how to trigger an AWS Lambda function when a new file arrives in an S3 bucket, offering a practical understanding of these services. The text culminates with an introduction to data governance, emphasizing its crucial role in data engineering projects.

**Key Insights**:
- AWS, launched in 2006, has been instrumental in shaping the cloud computing industry by continuously innovating and expanding its service offerings.
- Traditional data processing systems in organizations were complex, expensive, and required significant maintenance and scaling efforts, whereas AWS has simplified these challenges by providing on-demand and scalable solutions.
- AWS offers over 200 services, including analytics services, which data engineers can use to build complex data analytic pipelines.
- The chapter introduces key AWS-managed services for data ingestion, transformation, orchestration of big data pipelines, and data consumption, emphasizing the importance of selecting the right service for specific requirements.
- A hands-on component guides readers in triggering an AWS Lambda function when a new file arrives in an S3 bucket.


### Chapter 04, Data Cataloging, Security, and Governance 
In this chapter, the text explores the best practices for responsible data handling, aiming to ensure that data's value is fully realized by organizations. It covers various aspects of data governance, including data security, access, and privacy, data quality, data profiling, and data lineage. It introduces the significance of data catalogs and AWS services that aid in data governance. A hands-on component guides readers in configuring Lake Formation permissions, offering practical insights into implementing data governance. The chapter underscores the necessity of a robust data governance program to ensure correct data usage and its optimal value to the organization.

**Key Insights**:
- Data governance and security are crucial components of data management, ensuring that data remains secure, compliant with local laws, and discoverable for organizational use.
- Data breaches and mishandling can lead to reputational damage and government-imposed penalties, making it essential for organizations to prioritize responsible data handling.
- Siloed data, poor data quality, and a lack of user trust can hinder organizations from maximizing the value of their data.
- The hands-on component provides practical insights into configuring data governance in an AWS environment.


### Chapter 05, Architecting Data Engineering Pipelines
The chapter provides a structured approach to designing data pipelines, beginning with the importance of understanding data consumers and their specific requirements. It also covers the identification of data sources, the processes of data ingestion, and the essential steps of data transformation and optimization. Loading data into data marts is another critical component discussed, along with a practical hands-on session that guides readers in architecting a sample data pipeline. This chapter offers a comprehensive guide for translating data engineering concepts into real-world applications, enabling readers to bridge the gap between theory and practice.

**Key Insights**:
- Data pipelines are pivotal in data engineering, serving as the means to ingest data from multiple sources, optimize and transform it, and make it available to data consumers.
- The chapter focuses on the practical application of data engineering principles, enabling readers to translate theoretical knowledge into real-world data pipeline architecture.
- It emphasizes the importance of understanding the needs and requirements of data consumers as a fundamental step in the data pipeline design process.
- The chapter concludes with a hands-on exercise that allows readers to architect a sample data pipeline, providing practical experience in implementing the concepts covered.

 
### Chapter 06, Ingesting Batch and Streaming Data
The chapter covers several fundamental topics, including understanding data sources, ingesting data from database and streaming sources. It underscores the importance of using the right ingestion tools to ensure efficient data movement. The hands-on portion of the chapter allows readers to practice data ingestion from both database and streaming sources using AWS DMS, Amazon Kinesis, and AWS Glue.

**Key Insights**:
- Emphasizes the critical role of data ingestion within the data pipeline architecture, providing a detailed exploration of this foundational process.
- Data engineers often face the challenges of the five Vs of data: variety, volume, velocity, veracity, and value, and the chapter underscores the importance of addressing these challenges in data engineering.
- The chapter covers various data sources and the multitude of tools available within AWS for effective data ingestion.
- It provides guidance on making informed decisions when choosing the appropriate data ingestion tools for specific tasks.
- Readers gain practical experience through hands-on activities, ingesting data from both database and streaming sources using AWS DMS, Amazon Kinesis, and AWS Glue, reinforcing the theoretical concepts with practical application.


### Chapter 07, Transforming Data to Optimize for Analytics
This chapter looks into the vital task of data transformation, a key responsibility for data engineers in optimizing data for analytics and creating value for organizations. The chapter underscores the diversity of data transformations, distinguishing between common, generic transformations applicable to datasets, such as the conversion of raw files to Parquet format and partitioning, and those that incorporate business logic tailored to specific data content and business requirements. The chapter aims to equip data engineers with an understanding of the value of transformations, types of data transformation tools, common data preparation transformations, and business use case transformations. A hands-on section illustrates the practical application of these concepts, using AWS Glue Studio and Apache Spark for building transformations.

**Key Insights**:
- Data transformation is a key task for data engineers, involving various types of transformations, including both generic and business-specific ones.
- The chapter highlights the value of data transformations in optimizing data for analytics and creating value for organizations.
- It provides an overview of data transformation tools, common data preparation transformations, and business use case transformations.
- Hands-on activities with AWS Glue Studio and Apache Spark offer practical experience in building data transformations.
- The chapter serves as a bridge between data pipeline architecture and data ingestion, emphasizing the significance of data optimization for analytics in the data engineering process.


### Chapter 08, Identifying and Enabling Data Consumers
This chapter examines the intricacies of data consumers. Data consumers span a wide spectrum, from operational staff needing real-time stock levels to the CEO requiring data for strategic decision-making. Additionally, data consumers can be systems seeking data from other systems. The central objective of data engineers is to make datasets useful and accessible to these consumers, ultimately empowering the business to gain valuable insights from its data. To achieve this, data engineers must deliver the right data through appropriate tools to the right people or applications at the right time, facilitating informed decision-making. The chapter underscores the pivotal role of understanding business objectives, recognizing data consumers, and comprehending their requirements when designing a data engineering pipeline. This approach enables data engineers to select the right data ingestion tools, frequency, and transformation processes to meet the specific needs of data consumers. The chapter also considers data democratization, emphasizing its impact and significance. A hands-on section asks readers to take on the role of a data analyst tasked with creating a mailing list for the marketing department.

**Key Insights**:
- Data consumers, including individuals, applications, and systems within an organization, require access to data to fulfill a range of needs, from operational tasks to strategic decision-making.
- Data engineers play a crucial role in making datasets useful and accessible to data consumers, facilitating valuable insights for the business.
- Understanding the business objectives, identifying data consumers, and comprehending their requirements are essential steps in designing a data engineering pipeline.
- Data democratization has a significant impact on data access and usage, influencing various data consumer groups, including business users, data analysts, and data scientists.
- The hands-on section of the chapter provides practical experience in transforming data using AWS Glue DataBrew.


### Chapter 09, Loading Data into a Dart Mart
This chapter explores the significance of data warehouses and data marts in scenarios where data engineers need to move data from a data lake to an external data warehouse or data mart to serve specific data consumers. The chapter clarifies the distinctions between a data lake, which serves as a comprehensive source of truth across various business lines, and a data mart, which typically contains a subset of data tailored to specific user groups.
It begins by examining common anti-patterns that should be avoided when using data warehouses. Subsequently, it goes into the intricate architecture of Redshift, elucidating how it optimizes data storage across nodes. The chapter emphasizes the importance of design decisions for creating a Redshift cluster optimized for performance, as well as the processes for data ingestion into and unloading from Redshift. Additionally, advanced Redshift features, including data sharing, Data Distribution Keys (DDM), and cluster resizing, are reviewed. The hands-on exercises provide practical experience by guiding readers in creating a new Redshift Serverless cluster, exploring sample data, and configuring Redshift Spectrum to query data from Amazon S3. 

**Key Insights**:
- Data lakes provide a central source of data while data marts serve as subsets optimized for specific user groups and query types.
- Data marts play a dual role, offering a subset of data for targeted queries and providing high-performance query engines for analytic use cases.
- It highlights common anti-patterns to avoid in data warehouse usage and explores the architecture of Redshift, shedding light on its data storage optimization.
- Readers gain insights into the design considerations for high-performance data warehouses, data movement between data lakes and Redshift, and advanced Redshift features.
- The hands-on exercises involve creating a Redshift Serverless cluster and utilizing Redshift Spectrum for querying data from Amazon S3.

### Chapter 10, Orchestrating the Data Pipeline
This chapter explores the pivotal role of data pipeline orchestration tools in automating data engineering tasks, emphasizing their significance in a real production environment. The chapter begins by highlighting the various services and techniques discussed in previous chapters, including data ingestion via Amazon Kinesis Data Firehose and AWS Database Migration Service, as well as data transformation through AWS Lambda and AWS Glue functions. It underlines the importance of updating a data catalog and loading subsets of data into data marts or data warehouses for specific use cases. However, for real-world applications, manual triggering of these tasks is not acceptable, necessitating automation. Data pipeline orchestration engines play a crucial role in orchestrating various data engineering tasks, managing task sequences and dependencies, handling task success or failure, and executing tasks in parallel or sequentially. The chapter covers core concepts of pipeline orchestration, reviews different options for orchestrating data pipelines within AWS, and provides a hands-on activity demonstrating orchestration using AWS Step Functions.

Readers gain insights into concepts like scheduled and event-based pipelines, failure handling, and retries. The chapter introduces four AWS services for creating and orchestrating data pipelines, namely AWS Data Pipeline, AWS Glue workflows, Amazon MWAA, and AWS Step Functions. The hands-on section guides readers in building an event-driven pipeline using AWS Lambda functions and an Amazon SNS topic for notifications about failures, orchestrated by AWS Step Functions.

**Key Insights**:
- Data pipeline orchestration is crucial for automating data engineering tasks, enabling scheduled and event-driven pipelines, handling task failures, and orchestrating parallel and sequential tasks.
- Core concepts of pipeline orchestration, including scheduling and dependency management, are fundamental to designing effective data pipelines.
- AWS offers multiple orchestration options, including AWS Data Pipeline, AWS Glue workflows, Amazon MWAA, and AWS Step Functions, each with its unique strengths.
- The hands-on activity in this chapter involves orchestrating a data pipeline using AWS Step Functions, providing practical experience in implementing pipeline orchestration.
- This chapter serves as a bridge between architectural design and practical implementation of data pipelines, setting the stage for exploring data consumption services and deeper dives into data exploration and analysis in the subsequent chapters.


### Chapter 11, Ad Hoc Queries with Amazon Athena
This chapter investigates Amazon Athena, a serverless and fully managed service that allows users to query data directly in a data lake using SQL and Spark. The chapter commences by introducing Athena's features, emphasizing its setup-free nature, flexible payment options based on data scanned or provisioned capacity, and its capability to query data not only in data lakes but also from various other database sources using Query Federation. The chapter explores Athena's governance and cost management functionality through workgroups and offers recommended best practices for optimizing SQL queries for both cost-efficiency and performance.

The chapter also covers advanced functionality, illustrating how Athena can serve as a SQL query engine for data in Amazon S3 data lakes and external data sources like databases, data warehouses, and CloudWatch logs. It concludes with a hands-on exercise where users create an Athena workgroup, configure settings, and execute SQL queries within that workgroup.

**Key Insights**:
- Amazon Athena is a serverless, fully managed service that enables SQL and Spark-based querying of data in data lakes and various database sources.
- The chapter provides insights into optimizing Athena SQL queries for cost-efficiency and performance, covering tips and best practices.
- Athena's advanced functionality includes Query Federation, allowing users to query data from external sources like databases and data warehouses.
- Athena workgroups offer governance and cost management capabilities, helping manage settings for different teams or projects and controlling data scan limits in queries.


### Chapter 12, Visualizing Data with Amazon QuickSight
In this chapter, the focus is on Amazon QuickSight, a powerful BI tool that empowers users to create rich visualizations and reports while exploring data interactively. QuickSight offers features such as data filtering, drill-down capabilities, natural language querying, and the ability to summarize complex datasets visually. The chapter emphasizes the purpose of BI tools in helping users comprehend complex data through visual exploration. While it primarily covers Amazon QuickSight, the concepts discussed can apply to other popular BI applications like Tableau, Microsoft Power BI, and Qlik.

The chapter also looks at advanced QuickSight features, such as ML Insights for data trend detection and outlier identification, QuickSight Q for natural language querying, embedded dashboards for integration with websites and applications, and paginated reports. It concludes with a hands-on section guiding users through the configuration of QuickSight in their AWS account and the creation of customized visualizations. 

**Key Insights**:
- This chapter provides an in-depth understanding of Amazon QuickSight, highlighting its role as a serverless, fully managed BI tool for creating visualizations, analyzing data, and reporting.
- The chapter emphasizes the core concepts of business intelligence, explaining the significance of visual data representation, data exploration, and the role of BI tools in enabling users to make data-driven decisions.
- QuickSight's cost-effective subscription-based pricing model is discussed, making it a practical choice for organizations looking to avoid infrastructure and licensing costs.
- The chapter offers hands-on experience, guiding users through the setup and customization of QuickSight in their AWS accounts, empowering them to create their own visualizations and reports.


### Chapter 13, Enabling Artificial Intelligence and Machine Learning
This chapter delves into the significance of AI and ML for organizations, emphasizing how advancements in these fields have made it possible to automate tasks, personalize recommendations, and derive insights from data. While AI focuses on replicating human intelligence for tasks like problem-solving, decision-making, and language understanding, ML, more specifically, develops algorithms and models that recognize patterns in data to make predictions. The chapter highlights the growing impact of AI and ML in various domains, such as healthcare, self-driving vehicles, and the capabilities of Large Language Models (LLMs) like ChatGPT. It introduces AWS's array of AI and ML services and explores their utility with different data types.


**Key Insights**:
- The chapter underscores the transformative role of AI and ML in enabling organizations to automate tasks, personalize recommendations, and draw insights from data.
- It clarifies the distinction between AI and ML.
- The chapter introduces a range of AWS AI and ML services, including Amazon SageMaker for custom model development and services like Amazon Transcribe, Textract, Rekognition, and Comprehend for specific tasks.
- It explores various real-world applications of AI and ML, from early detection of diseases to self-driving vehicles and the capabilities of LLMs.
- The hands-on exercise in the chapter demonstrates the use of Amazon Comprehend for extracting insights from written text, providing practical exposure to AWS AI and ML services.


### Chapter 14, Transactional Data Lakes
In this chapter, the focus is on the evolution of data lakes, which have advanced significantly in recent years, transforming into transactional data lakes. These new technologies not only retain the benefits of traditional data lakes, such as cost-effectiveness and serverless data processing capabilities but also offer improved data update mechanisms.

The key topics covered in this chapter include defining the concept of a transactional data lake, an in-depth examination of table formats like Delta Lake, Apache Hudi, and Apache Iceberg, and how AWS integrates these table formats to create transactional data lakes. The hands-on section allows readers to work with Apache Iceberg tables in AWS, gaining practical experience in managing and querying tables in this modern data lake format.

**Key Insights**:
- Traditional data lakes built on Apache Hive had limitations in terms of handling data updates, querying consistency, and schema changes.
- New table formats like Delta Lake, Apache Hudi, and Apache Iceberg address these limitations, offering transactional capabilities and advanced features.
- AWS integrates these table formats to support the creation of transactional data lakes, making them more akin to traditional data warehouses.
- The transformation of data lakes into transactional data lakes is a significant shift, driven by innovations in table formats and metadata management, shaping the future of data lake management.

### Chapter 15, Implementing a Data Mesh strategy
This chapter introduces a shift from traditional data lake approaches to a newer concept known as a data mesh. Historically, organizations established central data engineering teams responsible for collecting, processing, and transforming raw data into a data lake. However, this centralized approach had its limitations. The data mesh approach presents an alternative by decentralizing data analytics and pushing the responsibility for creating analytic data products closer to the teams that generate or own the operational data. The chapter explores the various aspects of a data mesh, including organizational changes, architectural approaches, and technology implementation. It also delves into the core concepts and components of Amazon DataZone, a data governance tool offering a business data catalog. In a hands-on exercise, readers set up DataZone, import a dataset from the AWS Glue Data Catalog, add business metadata, and explore how to search the catalog and subscribe to data products.


**Key Insights**:
- The data mesh approach offers a decentralized model, pushing responsibility for data analytics closer to operational data owners.
- Data mesh implementation involves organizational changes, architectural approaches, and technology utilization.
- Amazon DataZone, a data governance tool with a business data catalog, is introduced as a key element in data mesh initiatives.
- The chapter provides a hands-on exercise for setting up DataZone, importing datasets, adding metadata, and exploring the catalog, preparing readers for modern data platform building on AWS.


### Chapter 16, Building a modern data platform on AWS
In this chapter, the focus is on the essential aspects of constructing a modern data platform on AWS. The chapter aims to provide a foundational understanding of building such platforms and emphasizes the significance of combining the various concepts presented throughout the book. It offers insights into goals for modern data platforms, deliberates the decision to build or buy such a platform, and introduces the concept of DataOps for automated development of data products. The hands-on section illustrates how AWS services like CloudFormation, CodeCommit, and CodePipeline can be employed to automate data platforms, streamlining infrastructure deployment and ETL code management.



**Key Insights**:
- Offers a high-level overview of constructing a modern data platform on AWS, serving as a foundational guide.
- Explores key objectives for modern data platforms, including flexibility, scalability, governance, security, and self-service capabilities.
- The chapter discusses the decision-making process of whether to build or purchase a data platform, weighing the pros and cons.
- Introduces DataOps as an approach to automate the development of data products and manage infrastructure, making the platform more efficient and agile.
- Demonstrates the practical use of AWS services like CloudFormation, CodeCommit, and CodePipeline to automate components and code deployment in a modern data platform.

### Chapter 17, Wrapping Up the First Part of Your Learning Journey
In this concluding chapter, the reader is reminded of the wide spectrum of topics explored in the book, ranging from common architectural patterns to hands-on experience with AWS services essential for data engineering. The chapter reflects on the significance of data engineering in optimizing data value within organizations. It emphasizes the dynamic nature of AWS services, with continuous innovation to meet evolving customer needs, offering a fast-paced journey through the cloud for data engineering platforms.

The chapter serves as an acknowledgment of the ever-expanding horizons of data engineering, indicating that the book is just the beginning of a comprehensive learning journey. It encourages the reader to delve deeper into the field. The conclusion paints an exciting picture of the journey ahead, implying that with the constant evolution of AWS services and the vast wealth of resources, the opportunities for growth and innovation are boundless for those venturing into data engineering on AWS.

**Key Insights**:
- The book provides a comprehensive exploration of data engineering, covering architectural patterns, hands-on AWS service usage, data security, governance, and data catalog importance.
- It introduces the concept of a data lake house and discusses data marts, data warehouses, and data consumers, along with tools like Amazon Athena and QuickSight for data querying and visualization.
- The book touches on ML and AI and highlights AWS services in these domains.
- Emerging trends such as the data mesh approach and open table formats like Apache Iceberg are discussed, focusing on decentralizing data engineering responsibilities.
- The chapter concludes by emphasizing the rapid evolution of AWS services and the constant learning opportunities in data engineering, encouraging readers to embark on a continuous learning journey in this field.

> If you feel this book is for you, get your [copy](https://www.amazon.in/Data-Engineering-AWS-cloud-based-transformation-ebook/dp/B0C61KXWQ5) today! <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">



## Learn more on the Discord server <img alt="Coding" height="25" width="32"  src="https://cliply.co/wp-content/uploads/2021/08/372108630_DISCORD_LOGO_400.gif">
You can join in on the discord server for all the latest updates and discussions in the community at [Discord](https://discord.gg/9s5mHNyECd)

## Download a free PDF <img alt="Coding" height="25" width="40" src="https://emergency.com.au/wp-content/uploads/2021/03/free.gif">

_If you have already purchased a print or Kindle version of this book, you can get a DRM-free PDF version at no cost. Simply click on the link to claim your free PDF._
[Free-Ebook](https://packt.link/free-ebook/9781804614426) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">

We also provide a PDF file that has color images of the screenshots/diagrams used in this book at [GraphicBundle](https://packt.link/gbp/9781804614426) <img alt="Coding" height="15" width="35"  src="https://media.tenor.com/ex_HDD_k5P8AAAAi/habbo-habbohotel.gif">


## Get to know the Author
_Gareth Eagar_  has over 25 years of experience in the IT industry, starting in South Africa, working in the United Kingdom for a while, and now based in the USA. Having worked at AWS since 2017, Gareth has broad experience with a variety of AWS services, and deep expertise around building data platforms on AWS. While Gareth currently works as a Solutions Architect, he has also worked in AWS Professional Services, helping architect and implement data platforms for global customers. Gareth also frequently speaks on data-related topics.


## Other Related Books
- [Data Engineering with dbt](https://www.packtpub.com/product/data-engineering-with-dbt/9781803246284)
- [Data Engineering with Python](https://www.packtpub.com/product/data-engineering-with-python/9781839214189)
