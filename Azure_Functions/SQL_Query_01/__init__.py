# Databricks notebook source
import logging
import pyodbc

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    # Connect to the Azure SQL database using PyODBC
    server = "globant-sql-server.database.windows.net"
    database = "globant_db"
    username = "admin_globant"
    password = "Rsw99787847@"
    driver = "{ODBC Driver 17 for SQL Server}"
    cnxn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")

    # Make the SQL query to get the number of employees hired for each job and department in 2021 divided by quarter
    query = """
    SELECT
        d.department,
        j.job,
        DATEPART(QUARTER, h.hire_date) AS quarter,
        COUNT(*) AS num_hires
    FROM
        hired_employees h
        JOIN departments d ON h.department_id = d.id
        JOIN jobs j ON h.job_id = j.id
    WHERE
        YEAR(h.datetime) = 2021
    GROUP BY
        d.department,
        j.job,
        DATEPART(QUARTER, h.datetime)
    ORDER BY
        d.department,
        j.job
    """

    # Execute the SQL query and fetch the results
    cursor = cnxn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()

    # Close the PyODBC connection
    cursor.close()
    cnxn.close()

    # Return the results as a JSON response
    results = []
    for row in rows:
        result = {
            "department": row[0],
            "job": row[1],
            "quarter": row[2],
            "num_hires": row[3]
        }
        results.append(result)
    return func.HttpResponse(json.dumps(results), mimetype="application/json", status_code=200)
