# Databricks notebook source
import logging
import pyodbc

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    
    #Set fileds required
    fields_hired_employees = ['id','name','datetime','department_id','job_id']
    fields_departaments = ['id','departament']
    fields_jobs = ['id','job']

    # Parse the request body as a list of dictionaries
    req_body = req.get_json()
    if isinstance(req_body, list):
           # Connect to the Azure SQL database using PyODBC
          server = "globant-sql-server.database.windows.net"
          database = "globant_db"
          username = "admin_globant"
          password = "Rsw99787847@"
          driver = "{ODBC Driver 17 for SQL Server}"
          cnxn = pyodbc.connect(f"DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}")
          cursor = cnxn.cursor()
   
        # Insert each item of every dictionary into the Azure SQL database table
        for dictionary in req_body:
            if dictionary['Table'] == 'hired_employees':
                if fields_hired_employees in dictionary:
                    for key, value in dictionary.items():
                        query = f"INSERT INTO hired_employees ({key}) VALUES (?)"
                        cursor.execute(query, value)
                        cnxn.commit()
                        
                    query = f"INSERT INTO Logs VALUES (hired_employees, {utc.now()}, Exitoso)"
                    cursor.execute(query)
                    cnxn.commit()
                else:
                    query = f"INSERT INTO Logs VALUES (hired_employees, {utc.now()}, Fallido)"
                    cursor.execute(query)
                    cnxn.commit()
                    
            elif dictionary['Table'] == 'departaments':
                if fields_departaments in dictionary:
                    for key, value in dictionary.items():
                        query = f"INSERT INTO departaments ({key}) VALUES (?)"
                        cursor.execute(query, value)
                        cnxn.commit()
                        
                    query = f"INSERT INTO Logs VALUES (departaments, {utc.now()}, Exitoso)"
                    cursor.execute(query)
                    cnxn.commit()
                else:
                    query = f"INSERT INTO Logs VALUES (departaments, {utc.now()}, Fallido)"
                    cursor.execute(query)
                    cnxn.commit()
                    
            elif dictionary['Table'] == 'jobs':
                if fields_jobs in dictionary:
                    for key, value in dictionary.items():
                        query = f"INSERT INTO jobs ({key}) VALUES (?)"
                        cursor.execute(query, value)
                        cnxn.commit()
                        
                    query = f"INSERT INTO Logs VALUES (jobs, {utc.now()}, Exitoso)"
                    cursor.execute(query)
                    cnxn.commit()
                else:
                    query = f"INSERT INTO Logs VALUES (jobs, {utc.now()}, Fallido)"
                    cursor.execute(query)
                    cnxn.commit()
            else:
                print('Wrong Table')

        # Close the PyODBC connection and return a success response
        cursor.close()
        cnxn.close()
        return func.HttpResponse("Data successfully inserted into Azure SQL table.", status_code=200)

    else:
        return func.HttpResponse("Invalid request body.", status_code=400)
