import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

schemaName = "DB2ADMIN"
resultSet = ibm_db.tables(conn, None, schemaName, 'TAB%', 'TABLE')
dataRecord = ibm_db.fetch_assoc(resultSet)
while dataRecord:
    print("Table schema  : {}" .format(dataRecord['TABLE_SCHEM']))
    print("Table name    : {}" .format(dataRecord['TABLE_NAME']))
    print("Table type    : {}" .format(dataRecord['TABLE_TYPE']))
    print("Description   : {}" .format(dataRecord['REMARKS']))
    dataRecord = ibm_db.fetch_assoc(resultSet)
    print("------------------------------------------------------")
