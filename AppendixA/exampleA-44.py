import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', ,{ibm_db.SQL_ATTR_AUTOCOMMIT: bm_db.SQL_AUTOCOMMIT_OFF})

sql = "insert into tabmany values(100, 'Testrollback')"
stmt = ibm_db.exec_immediate(conn, sql)
sql = "select name from tabmany where id=100"
stmt = ibm_db.exec_immediate(conn, sql)
res = ibm_db.fetch_tuple(stmt)
print(res)

# rollback
rc = ibm_db.rollback(conn)

# again fetch the data, should see empty row
stmt1 = ibm_db.exec_immediate(conn, sql)
res1 = ibm_db.fetch_tuple(stmt1)
print(res1)
