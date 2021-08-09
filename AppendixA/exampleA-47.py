import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

schemaName = "DB2ADMIN"
tableName = "TABMANY"
resultSet = ibm_db.special_columns(conn, None, schemaName, tableName, 0)
dataRecord = ibm_db.fetch_assoc(resultSet)
while dataRecord:
    print("Column name            : {}" .format(dataRecord['COLUMN_NAME']))
    print("Data type              : {}" .format(dataRecord['TYPE_NAME']))
    print("Column size            : {}" .format(dataRecord['COLUMN_SIZE']))	
