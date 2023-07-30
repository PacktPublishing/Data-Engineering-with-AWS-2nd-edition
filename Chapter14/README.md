# Chapter 14 - Building Transactional Data Lakes

In this chapter we did a deeper-dive into three common transactional table formats (also sometimes refered to as open table formats), namely Delta
Lake, Apache Hudi, and Apache Iceberg. 

We looked into the limitations of the traditional Hive format, and discussed how these new transactional formats provided a number of benefits for
building modern data lakes, that are able to behave more like a traditional data warehouse. We discussed benefits such as being able to use
ACID transactions, perform record level updates, run time travel queries, handle schema evolution, and more. 

We then 'looked under the covers' at how these open table formats work by tracking metadata at the table level, and at some of the different
approaches for performing updates - Copy-on-Write (COW) which provides better read performance, and Merge-on-Read (MOR) that provides better
write performance. 

Each of the three popular table formats we discussed in this section have their own pros and cons, and while there was not space to go super
deep into how each of them work, we did do a bit of a deeper dive into Delta Lake, Apache Hudi and Apache Iceberg. Finally, before getting hands-on,
we reviewed the support for each of the table formats across different AWS services (such as Glue, EMR, Redshift, and Athena). 

## Hands-on Activity
In the hands-on activity section of this chapter, we used Amazon Athena to create an Apache Iceberg formatted table, added data to the table,
and then looked at how the underlying metadata was changed as we deleted data and performed table maintenance tasks. We also used the time travel
feature of Iceberg to see how we could query data as it was at a previous point in time. 

#### Creating an Apache Iceberg table using Amazon Athena

- Amazon Management Console - Athena: https://console.aws.amazon.com/athena/home

- Use the following statement to create a new Athena database
```
create database curatedzonedb_iceberg;
```

- Use the following statement to create a new table in Apache Iceberg format. **Make sure to change the S3 bucket location below to
match the location of your curated-zone bucket**.
```
CREATE TABLE curatedzonedb_iceberg.streaming_films_ib(
	timestamp string,
	eventtype string,
	film_id_streaming int,
	distributor string,
	platform string,
	state string,
	ingest_year string,
	ingest_month string,
	category_id bigint,
	category_name string,
	film_id bigint,
	title string,
	description string,
	release_year bigint,
	language_id bigint,
	original_language_id double,
	length bigint,
	rating string,
	special_features string
)
PARTITIONED BY (category_name)
LOCATION 's3://dataeng-curated-zone-gse23/iceberg/streaming_films/'
TBLPROPERTIES ('table_type' = 'ICEBERG', 'format' = 'parquet')
```

- Access the Amazon S3 console to review metadata files: https://s3.console.aws.amazon.com/s3

#### Adding data to our Iceberg table and running queries

- Run the following statement to insert data from the previously created streaming_films table (created in Chapter 7), into our new
Apache Iceberg formatted table created in the previous step.
```
insert into curatedzonedb_iceberg.streaming_films_ib
select *
from curatedzonedb.streaming_films
```

- Open the AWS Glue console to view table properties: https://console.aws.amazon.com/glue

- Run the following statement to query the newly created table
```
select * from curatedzonedb_iceberg.streaming_films_ib limit 50;
```

- Run the following three statements (one at a time) to view table metadata.
```
select * from "curatedzonedb_iceberg"."streaming_films_ib$manifests"
```

```
select * from "curatedzonedb_iceberg"."streaming_films_ib$files"
```

```
select * from "curatedzonedb_iceberg"."streaming_films_ib$partitions"
```

#### Modifying data in our Iceberg table and running queries

- Delete data from the table for all movies in the *Documentary* category, using the following statement
```
delete from curatedzonedb_iceberg.streaming_films_ib where category_name='Documentary'
```

- Use the following statement to list out the current partitions, and note how there are only 15 partitions now
```
select * from "curatedzonedb_iceberg"."streaming_films_ib$partitions"
```

- Use the following statement to list out details about the current manifest:
```
select * from "curatedzonedb_iceberg"."streaming_films_ib$manifests"
```
- Use the following statemet to query the snapshot history:

```
select * from "curatedzonedb_iceberg"."streaming_films_ib$history"
```

- Use the following statement to do a *time travel* query, where you query the table as it was at a point in the past
```
SELECT * FROM "curatedzonedb_iceberg"."streaming_films_ib" FOR TIMESTAMP AS OF TIMESTAMP '2023-07-23 19:00:00 UTC' where category_name = 'Documentary'
```

#### Iceberg table maintenance tasks

- Use the following statement to display the list of files that make up the current snapshot:
```
select * from "curatedzonedb_iceberg"."streaming_films_ib$files"
```

- Execute the OPTIMIZE command by running the following statemet:
```
OPTIMIZE curatedzonedb_iceberg.streaming_films_ib REWRITE DATA USING BIN_PACK
```

-- Use the following statement to display the list of files that make up the current, optimized, snapshot:
```
select * from "curatedzonedb_iceberg"."streaming_films_ib$files"
```

- Use the following statement to list the tables snapshot history:
```
select * from "curatedzonedb_iceberg"."streaming_films_ib$history"
```

- Change the table property for `vacuum_max_snapshot_age_seconds` to be just 60 seconds

```
ALTER TABLE curatedzonedb_iceberg.streaming_films_ib SET TBLPROPERTIES (
  'vacuum_max_snapshot_age_seconds'='60'
)
```

- View the properties of our Iceberg table to ensure that the setting was applied:

```
SHOW TBLPROPERTIES curatedzonedb_iceberg.streaming_films_ib
```

- Run the following statement to VACUUM the Iceberg table

```
VACUUM curatedzonedb_iceberg.streaming_films_ib
```









