import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

schemaName = 'DB2ADMIN'
resultSet = ibm_db.procedures(conn, None, schemaName, 'PROC')
row = ibm_db.fetch_assoc(resultSet)
while row:
    print(row)
    row = ibm_db.fetch_assoc(resultSet)
