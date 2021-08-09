import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

result = ibm_db.exec_immediate(conn, "select * from tabmany")
for i in range(0, ibm_db.num_fields(result) ):
    col_width = ibm_db.field_width(result, i)
    col_name = ibm_db.field_name(result,i)
    #print(col_name,col_width)
    print("{:<{width}}".format(col_name, width=col_width),end=" ")
