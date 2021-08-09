import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')


sql = "select id, name from tabmany"
field_name=[]
stmt = ibm_db.prepare(conn, sql,)
result = ibm_db.execute(stmt)
cols = ibm_db.num_fields(stmt)
for i in range(0, cols):
    field_name.append(ibm_db.field_name(stmt,i))
print(field_name)
