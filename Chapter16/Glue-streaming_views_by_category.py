import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Load the streaming_films table into a Glue DynamicFrame from the Glue catalog
StreamingFilms = glueContext.create_dynamic_frame.from_catalog(
    database="curatedzonedb",
    table_name="streaming_films",
    transformation_ctx="StreamingFilms",
)

# Convert the DynamicFrame to a Spark DataFrame
spark_dataframe = StreamingFilms.toDF()

# Create a SparkSQL table based on the steaming_films table
spark_dataframe.createOrReplaceTempView("streaming_films")

# Create a new DataFrame that records number of streams for each
# category of film
CategoryStreamsDF = glueContext.sql("""
SELECT category_name,
         count(category_name) streams
FROM streaming_films
GROUP BY category_name
""")

# Convert the DataFrame back to a Glue DynamicFrame
CategoryStreamsDyf = DynamicFrame.fromDF(CategoryStreamsDF, glueContext, "CategoryStreamsDyf")

# Prepare to write the dataframe to Amazon S3
############# NOTE ############# 
#### Change the path below to
#### reference your bucket name
################################
s3output = glueContext.getSink(
  path="s3://dataeng-curated-zone-gse23/streaming/top_categories",
  connection_type="s3",
  updateBehavior="UPDATE_IN_DATABASE",
  partitionKeys=[],
  compression="snappy",
  enableUpdateCatalog=True,
  transformation_ctx="s3output",
)
# Set the database and table name for where you want this table
# to be registered in the Glue catalog
s3output.setCatalogInfo(
  catalogDatabase="curatedzonedb", catalogTableName="category_streams"
)
# Set the output format to Glue Parquet
s3output.setFormat("glueparquet")
# Write the output to S3 and update the Glue catalog
s3output.writeFrame(CategoryStreamsDyf)
job.commit()
