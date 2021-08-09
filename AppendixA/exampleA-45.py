import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

serverInfo = ibm_db.server_info(conn)
print("Db2 database server name                 : {}" .format(serverInfo.DBMS_NAME))
print("Database name                            : {}" .format(serverInfo.DB_NAME))
print("Db2 instance name                        : {}" .format(serverInfo.INST_NAME))
print("Database codepage used                   : {}" .format(serverInfo.DB_CODEPAGE))
