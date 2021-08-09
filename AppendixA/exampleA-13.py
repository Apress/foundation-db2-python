import ibm_db
dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')
database='test123'
conn_attach = ibm_db.connect(conn_str_attach, '', '')
rc = ibm_db.createdb(conn_attach, database)
