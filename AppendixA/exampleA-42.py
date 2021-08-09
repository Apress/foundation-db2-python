import ibm_db
conn_str_attach = "attach=true;HOSTNAME=hostname;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
database='test123'
conn_attach = ibm_db.connect(conn_str_attach, '', '')

rc = ibm_db.recreatedb(conn_attach, database)
