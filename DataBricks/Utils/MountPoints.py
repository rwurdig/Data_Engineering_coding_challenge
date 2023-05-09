# Databricks notebook source
# MAGIC %md
# MAGIC #MountPoints

# COMMAND ----------

# DBTITLE 1,Creation of MountPoints
#Deff of Containers
containers=['gold','silver','bronze'] 

#Set Storage Information
Storage = 'adlsglobantdb'
key = dbutils.secrets.get(scope="Sc-Scope", key="dataLake-datahub-accessKey") 
#key = "xRPmvPEnueIHz5ecL5o7DqCeCeSmdBaqquXOBC5T40z7aza35L9ohZRSoPdO2c6jmMPq7Yr/b4zH+ASt579jsQ=="

#Create Mount Points
for cont in containers:
    dbutils.fs.mount(
              source = f"wasbs://{cont}@{Storage}.blob.core.windows.net",
              mount_point = f"/mnt/{cont}",
              extra_configs = {f"fs.azure.account.key.{Storage}.blob.core.windows.net":key })

# COMMAND ----------

# DBTITLE 1,List availible MountPoints
# MAGIC %fs
# MAGIC mounts
