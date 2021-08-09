import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
stmt = ibm_db.exec_immediate(conn, sql)

row = ibm_db.fetch_tuple(stmt)
while ( row ):
    for i in row:
         print(i)
    row = ibm_db.fetch_tuple(stmt)
ibm_db.close(conn)
