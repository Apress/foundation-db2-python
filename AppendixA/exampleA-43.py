import ibm_db
conn=ibm_db.connect("DATABASE=database;HOSTNAME=hostname;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password",'','')

sql = "select id, name from tabmany"
stmt = ibm_db.exec_immediate(conn, sql)
while (ibm_db.fetch_row(stmt)):
    id = ibm_db.result(stmt, "ID")
    name = ibm_db.result(stmt, "NAME")
    print("col1 = {}, col2 = {}".format(id, name))
