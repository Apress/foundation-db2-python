import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

result = ibm_db.exec_immediate(conn, "select * from tabmany")
for i in range(0, ibm_db.num_fields(result) ):
    print(str(i) + ":" + str(ibm_db.field_type(result,i)))
