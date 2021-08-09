import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
stmt = ibm_db.prepare(conn, sql,)
result = ibm_db.execute(stmt)
cols = ibm_db.num_fields(stmt)
print(cols)
