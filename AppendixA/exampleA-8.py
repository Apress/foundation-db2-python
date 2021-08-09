import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')

# TABMANY is table name
result = ibm_db.columns(conn,None,None,"TABMANY")
row = ibm_db.fetch_both(result)
if row:
    table_name=row['TABLE_NAME']
    column_name=row['COLUMN_NAME']
print("Table name               : {}" .format(table_name))
print("column name              : {}" .format(column_name))
