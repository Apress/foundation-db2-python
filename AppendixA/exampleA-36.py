import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "update tabmany set id=15 where id < 40"
res = ibm_db.exec_immediate(conn, sql)
print ("Number of affected rows: %d" % ibm_db.num_rows(res))
ibm_db.rollback(conn)
ibm_db.close(conn)
