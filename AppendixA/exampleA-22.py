import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
stmt = ibm_db.prepare(conn, sql,)
result = ibm_db.execute(stmt)
row = ibm_db.fetch_both(stmt)
while ( row ):
    print("%-5d %-5d " % (row['ID'], row[0]))
    print("%-16s %-16s " % (row['NAME'], row[1]))
    row = ibm_db.fetch_both(stmt)
