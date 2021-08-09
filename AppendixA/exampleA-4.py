import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')

sql = "create or replace procedure proc(OUT out1 integer) dynamic result sets 1 "
sql += "begin select id into out1 from tabmany where id=1; end"
ibm_db.exec_immediate(conn, sql)
out1 = 0
stmt, out1 = ibm_db.callproc(conn,'proc',(out1,))
print(out1)

proc2 = "CREATE PROCEDURE out_blob(IN P1 BLOB(100),OUT P2 BLOB(100)) "
proc2 += "LANGUAGE SQL DYNAMIC RESULT SETS 0 BEGIN SET P2 = P1; END""
result = ibm_db.exec_immediate(conn, proc2)
stmt, blob1, blob2 = ibm_db.callproc(conn, 'out_blob', (b'1234',b'0'))

if stmt is not None:
    print("Values of bound parameters _after_ CALL:")
    print("  1: %s\t 2: %s \n" % (blob1, blob2))
