# Databricks notebook source
# DBTITLE 1,Set Libraries
import pyspark
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType,StructField, StringType, IntegerType
from delta.tables import *
from delta.tables import DeltaTable

# COMMAND ----------

# DBTITLE 1,Set SparkConfigurations
spark = SparkSession.builder.master("local[1]") \
                    .appName('SparkByExamples.com') \
                    .getOrCreate()

# COMMAND ----------

# DBTITLE 1,Functions
def file_exists(path):
    """ Check if path exists 
         Params: Path File
    """
    try:
        dbutils.fs.ls(path)
        return True
    except Exception as e:
        if 'java.io.FileNotFoundException' in str(e):
            return False
        else:
            raise

# COMMAND ----------

# DBTITLE 1,Set Variables
Landing_hired_employees = '/mnt/bronze/Historical/hired_employees.csv'
Landing_departaments = '/mnt/bronze/Historical/departments.csv'
Landing_jobs = '/mnt/bronze/Historical/jobs.csv'

Silver_hired_employees = '/mnt/silver/Tables/HiredEmployees/'
Silver_departaments = '/mnt/silver/Tables/Departments/'
Silver_jobs = '/mnt/silver/Tables/Jobs/'

Gold_hired_employees = '/mnt/gold/HiredEmployees/'
Gold_departaments = '/mnt/gold/Departments/'
Gold_jobs = '/mnt/gold/Jobs/'

# Define the connection parameters to your Azure SQL database
jdbc_url = "jdbc:sqlserver://globant-sql-server.database.windows.net:1433;database=globant_db"
mode = "overwrite"
properties = {
    "user": "admin_globant",
    "password": f"{dbutils.secrets.get(scope="Sc-Scope", key="Sql-Server-Password")}",
    "driver": "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

#"password": "passwordRsw99787847@",

# COMMAND ----------

# DBTITLE 1,Def Schema from tables
#Schema for Hired Employees
Schema_hired_employees = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("name",StringType(),True), \
    StructField("datetime",StringType(),True), \
    StructField("department_id", IntegerType(), True), \
    StructField("job_id", IntegerType(), True) \
  ])

#Schema for Departments
Schema_departaments = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("departament",StringType(),True) \
  ])

#Schema for Jobs
Schema_jobs = StructType([ \
    StructField("id",IntegerType(),True), \
    StructField("job",StringType(),True) \
  ])

# COMMAND ----------

# DBTITLE 1,Create Dataframes
hired_employees_df = spark.read.csv(Landing_hired_employees, header='False', schema = Schema_hired_employees)

departaments_df = spark.read.csv(Landing_departaments, header='False', schema = Schema_departaments)

jobs_df = spark.read.csv(Landing_jobs, header='False', schema = Schema_jobs)

# COMMAND ----------

# DBTITLE 1, Write tables to Silver
hired_employees_df.write.format("parquet").mode('overwrite').parquet(Silver_hired_employees)

departaments_df.write.format("parquet").mode('overwrite').parquet(Silver_departaments)

jobs_df.write.format("parquet").mode('overwrite').parquet(Silver_jobs)

# COMMAND ----------

# DBTITLE 1,Write for first time in gold
if file_exists(Gold_hired_employees):
    gold_hired_employees_df = DeltaTable.forPath(spark, f'{Gold_hired_employees}')
    print('Table Hired Employees already exist')
else:
    hired_employees_df.write.format("delta").mode('overwrite').save(Gold_hired_employees)
    gold_hired_employees_df = DeltaTable.forPath(spark, f'{Gold_hired_employees}')

    
if file_exists(Gold_departaments):
    gold_departaments_df = DeltaTable.forPath(spark, f'{Gold_departaments}')
    print('Table Departments already exist')
else:
    departaments_df.write.format("delta").mode('overwrite').save(Gold_departaments)
    gold_departaments_df = DeltaTable.forPath(spark, f'{Gold_departaments}')

    
if file_exists(Gold_jobs):
    gold_jobs_df = DeltaTable.forPath(spark, f'{Gold_jobs}')
    print('Table Jobs already exist')
else:
    jobs_df.write.format("delta").mode('overwrite').save(Gold_jobs)
    gold_jobs_df = DeltaTable.forPath(spark, f'{Gold_jobs}')

# COMMAND ----------

# DBTITLE 1,Merge Tables Silver to Gold
gold_hired_employees_df \
                    .alias("gold") \
                    .merge(
                        hired_employees_df.alias("silver"),
                        f"gold.id = silver.id"
                    ) \
                    .whenMatchedUpdateAll() \
                    .whenNotMatchedInsertAll() \
                    .execute()

gold_departaments_df \
                    .alias("gold") \
                    .merge(
                        departaments_df.alias("silver"),
                        f"gold.id = silver.id"
                    ) \
                    .whenMatchedUpdateAll() \
                    .whenNotMatchedInsertAll() \
                    .execute()

gold_jobs_df \
                    .alias("gold") \
                    .merge(
                        jobs_df.alias("silver"),
                        f"gold.id = silver.id"
                    ) \
                    .whenMatchedUpdateAll() \
                    .whenNotMatchedInsertAll() \
                    .execute()

# COMMAND ----------

# DBTITLE 1,Write into SQL DB
table_name_hired_employees = "hired_employees"
hired_employees_df.write.jdbc(url=jdbc_url, table=table_name_hired_employees, mode=mode, properties=properties)

table_name_departaments = "departaments"
departaments_df.write.jdbc(url=jdbc_url, table=table_name_departaments, mode=mode, properties=properties)

table_name_jobs = "jobs"
jobs_df.write.jdbc(url=jdbc_url, table=table_name_jobs, mode=mode, properties=properties)
