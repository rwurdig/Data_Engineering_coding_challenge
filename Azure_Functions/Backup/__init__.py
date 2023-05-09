# Databricks notebook source
import logging
import os
import pyodbc
import pandas as pd
from azure.storage.blob import BlobServiceClient

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Connect to the Azure SQL database using PyODBC
    server = "globant-sql-server.database.windows.net"
    database = "globant_db"
    username = "admin_globant"
    password = "Rsw99787847@"
    driver = "{ODBC Driver 17 for SQL Server}"
    cnxn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")

    # Connect to the Azure Storage account using the BlobServiceClient
    connection_string = "DefaultEndpointsProtocol=https;AccountName=adlsglobantdb;AccountKey=xRPmvPEnueIHz5ecL5o7DqCeCeSmdBaqquXOBC5T40z7aza35L9ohZRSoPdO2c6jmMPq7Yr/b4zH+ASt579jsQ==;EndpointSuffix=core.windows.net"
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)

    # Get a reference to the container where the backup files will be stored
    container_name = "silver"
    container_client = blob_service_client.get_container_client(container_name)

    # Get a list of table names from the Azure SQL database
    cursor = cnxn.cursor()
    cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE='BASE TABLE'")
    table_names = cursor.fetchall()

    # Serialize the data from each table and save it in a CSV file in Azure Storage
    for table_name in table_names:
      query = f"SELECT * FROM {table_name[0]}"
      df = pd.read_sql_query(query, cnxn)
      
      # Save the data from the table as a CSV file
      filename = f"{table_name[0]}.csv"
      file_path = os.path.join(os.environ["TMP"], filename)
      df.to_csv(file_path, index=False)


      # Upload the CSV file to Azure Storage
      with open(file_path, "rb") as csv_file:
        blob_client = container_client.get_blob_client(filename)
        blob_client.upload_blob(csv_file, overwrite=True)


      # Delete the local CSV file
      os.remove(file_path)

    # Close the PyODBC connection and return a success response
    cursor.close()
    cnxn.close()
    return func.HttpResponse("Backup successfully created for all tables in Azure SQL database.", status_code=200)
