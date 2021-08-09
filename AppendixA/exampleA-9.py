import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')

#set autocommit off
rc = ibm_db.autocommit(conn, ibm_db.SQL_AUTOCOMMIT_OFF)

#insert a row 
stmt = ibm_db.exec_immediate(conn, "insert into tabmany values(2, 'commit test')")

#commit the transaction explicitly as autocommit is off
rc = ibm_db.commit(conn)

#validate that row is inserted
sql_stmt = ibm_db.exec_immediate(conn, "select * from tabmany")
row = ibm_db.fetch_tuple(sql_stmt)
if row:
    print(str(row[0]) + "\n" + row[1])

#close the connection
ibm_db.close(conn)
