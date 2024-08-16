import pandas as pd
import pyodbc

conn_string="Driver=ODBC Driver 18 for SQL Server;Server=tcp:serveru123.database.windows.net,1433;Database=DB123;Uid=server123-UID;Pwd=P@ssword;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
connection=pyodbc.connect(conn_string)
df1=pd.read_sql_query("""Select * from digi""",connection)
print(df1)
print("Hellow world")
print("Good to see you")
