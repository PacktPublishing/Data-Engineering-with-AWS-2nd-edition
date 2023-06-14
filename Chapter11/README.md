# Chapter 11 - Ad-hoc queries with Amazon Athena

Amazon Athena is a serverless, fully managed service that lets you use SQL to directly query data in the data lake, as well as query various other databases. It requires no setup, and by default the cost is based  on the amount of data that is scanned to complete the query, or based on the amount of provisioned capacity that you specify. 

In this chapter, we did a deep dive into Athena, examining how Athena can be used to query data directly in the data lake, looking at advanced Athena functionality (such as the ability to query data from other data sources with Query Federation), and how Athena provides workgroup functionality to help with governance and cost management.

## Links
[Considerations and Limitations for CTAS Queries](https://docs.aws.amazon.com/athena/latest/ug/considerations-ctas.html)

[Airbnb blog post about the problem of small files](https://medium.com/airbnb-engineering/on-spark-hive-and-small-files-an-in-depth-look-at-spark-partitioning-strategies-a9a364f908)

[Partitioning and bucketing in Athena](https://docs.aws.amazon.com/athena/latest/ug/ctas-partitioning-and-bucketing.html)

[Partition Projection with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/partition-projection.html)

[Using EXPLAIN and EXPLAIN ANALYSE in Athena](https://docs.aws.amazon.com/athena/latest/ug/athena-explain-statement.html)

[Functions in Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/functions.html)

[Performance Tuning in Athena](https://docs.aws.amazon.com/athena/latest/ug/performance-tuning.html)

[Using Amazon Athena Federated Query](https://docs.aws.amazon.com/athena/latest/ug/connect-to-a-data-source.html)

[Athena Query Federation SDK](https://docs.aws.amazon.com/athena/latest/ug/connect-data-source-federation-sdk.html)

[Explore your data lake using Amazon Athena for Apache Spark](https://aws.amazon.com/blogs/big-data/explore-your-data-lake-using-amazon-athena-for-apache-spark/)

[Using Athena ACID transactions](https://docs.aws.amazon.com/athena/latest/ug/acid-transactions.html)

[Tag-Based IAM Access Control Policies](https://docs.aws.amazon.com/athena/latest/ug/tags-access-control.html)

## Hands-on Activity

In the hands-on activity section of this chapter, we create and configure a new Athena Workgroup and learn more about how Workgroups can help separate groups of users.

#### Creating an Amazon Athena workgroup and configuring Athena settings

- AWS Management Console - Amazon Athena: https://console.aws.amazon.com/athena

#### Switching Workgroups and running queries

- AWS Documentation on IAM Policies for Accessing Workgroups: https://docs.aws.amazon.com/athena/latest/ug/workgroups-iam-policy.html

- Query to determine most popular category of films (Step 3)
```
SELECT category_name, count(category_name) streams
FROM streaming_films
GROUP BY category_name
ORDER BY streams DESC
```

- Query to determine which State streamed the most films (Step 7)
```
SELECT state, count(state) count
FROM streaming_films
GROUP BY state
ORDER BY count desc
```






