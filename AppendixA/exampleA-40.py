import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql="""create or replace procedure proc(OUT out1 integer) dynamic result sets 1 begin  select id into out1 from tabmany where id=1; end"""
ibm_db.exec_immediate(conn, sql)
# note the procedure name upper case
resultSet = ibm_db.procedure_columns(conn, None, '', 'PROC', None)
#print(resultSet)
row = ibm_db.fetch_assoc(resultSet)
while row:
    print(row)
    print("Procedure {} is having one output parameter with name {}\n".format(row['PROCEDURE_NAME'], row['COLUMN_NAME']))
    row = ibm_db.fetch_assoc(resultSet)
