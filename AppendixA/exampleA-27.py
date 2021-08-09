import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
field_precision=[]
stmt = ibm_db.prepare(conn, sql,)
result = ibm_db.execute(stmt)
cols = ibm_db.num_fields(stmt)
for i in range(0, cols):
    field_precision.append(ibm_db.field_precision(stmt,i))
print(field_precision)

row = ibm_db.fetch_tuple(stmt)
# use the precision to format the data display
print("{:<{prec}}\t{:>{char_prec}}". \
 format(row[0],row[1],prec=field_precision[0],char_prec=field_precision[1]))
