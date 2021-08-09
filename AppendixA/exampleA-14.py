import ibm_db

database='test123'
dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')
rc = ibm_db.createdbNX(conn_attach, database) ibm_db.cursor_type
