import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

insert = "insert into scale_test values(25280.00, 17600.00)"
ibm_db.exec_immediate(conn, insert)

sql = "select salary, bonus from scale_test"
field_scale=[]
stmt = ibm_db.prepare(conn, sql)
result = ibm_db.execute(stmt)
cols = ibm_db.num_fields(stmt)
for i in range(0, cols):
    field_scale.append(ibm_db.field_scale(stmt,i))
print(field_scale)
row = ibm_db.fetch_tuple(stmt)
print("{:<{scale1}}\t{:>{scale2}}". \ format(row[0],row[1],scale1=field_scale[0],scale2=field_scale[1]))
