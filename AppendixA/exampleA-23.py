import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
stmt = ibm_db.prepare(conn, sql,)
result = ibm_db.execute(stmt)
row = ibm_db.fetch_row(stmt)
while ( row ):
    print(row)
    row = ibm_db.fetch_row(stmt)
