import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')
stmt=ibm_db.prepare(conn, "select * from tabmany where id=?")
id=1
ibm_db.bind_param(stmt, 1, id)
ibm_db.execute(stmt)
row=ibm_db.fetch_tuple(stmt)
print(row)
