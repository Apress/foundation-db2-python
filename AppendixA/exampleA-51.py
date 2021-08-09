import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

schemaName = "DB2ADMIN"
tableName = "TABMANY"
resultSet = ibm_db.table_privileges(conn, None, schemaName, tableName)
dataRecord = ibm_db.fetch_assoc(resultSet)
print("Schema name            : {}" .format(dataRecord['TABLE_SCHEM']))
print("Table name             : {}" .format(dataRecord['TABLE_NAME']))
print("Privilege grantor      : {}" .format(dataRecord['GRANTOR']))
print("Privilege recipient    : {}" .format(dataRecord['GRANTEE']))
print("Privilege              : {}" .format(dataRecord['PRIVILEGE']))
print("Privilege is grantable : {}" .format(dataRecord['IS_GRANTABLE']))
