import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

result = ibm_db.exec_immediate(conn, "select * from tabmany")
row = ibm_db.fetch_both(result)
while row:
    print(row)
    row = ibm_db.fetch_both(result)
	
ibm_db.free_result(result)
