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

    # Make the SQL query to get the list of department IDs, names, and number of employees hired by each department that hired more employees than the mean of employees hired in 2021 for all departments, ordered by the number of employees hired (descending)
    query = """
    SELECT
        d.id,
        d.department,
        COUNT(*) AS num_hires
    FROM
        hired_employees h
        JOIN departments d ON h.department_id = d.id
    WHERE
        YEAR(h.datetime) = 2021
    GROUP BY
        d.id,
        d.department
    HAVING
        COUNT(*) > (SELECT AVG(num_hires) FROM (SELECT COUNT(*) AS num_hires FROM hired_employees WHERE YEAR(datetime) = 2021 GROUP BY department_id) AS dept_hires)
    ORDER BY
        num_hires DESC
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
            "department_id": row[0],
            "department": row[1],
            "num_hires": row[2]
        }
        results.append(result)
    return func.HttpResponse(json.dumps(results), mimetype="application/json", status_code=200)
