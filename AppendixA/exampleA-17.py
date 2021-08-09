import ibm_db
import pandas as pd
import ibm_db_dbi as dbi

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql_stmt =  "select * from tabmany"
result = ibm_db.exec_immediate(conn, sql_stmt)
if stmt is not None:
    row = ibm_db.fetch_tuple(result)
    while(row):
        print("{}\t{}\n".format(row[0],row[1])
        row = ibm_db.fetch_tuple(result)

# use pandas dataframe
conn1 = dbi.connect(dbstring)
df = pd.read_sql("select * from tabmany", conn1)
print(df)
