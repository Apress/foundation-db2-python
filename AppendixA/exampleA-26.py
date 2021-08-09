import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
field_num=[]
field_name=[]
stmt = ibm_db.prepare(conn, sql,)
result = ibm_db.execute(stmt)
cols = ibm_db.num_fields(stmt)

# index by column number
for i in range(0, cols):
    field_name.append(ibm_db.field_name(stmt,i))
    field_num.append(ibm_db.field_num(stmt,field_name[i]))
print(field_num)

# index by column name
field_num=[]
field_num.append(ibm_db.field_num(stmt, 'ID'))
field_num.append(ibm_db.field_num(stmt, 'NAME'))
print(field_num)
