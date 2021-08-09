import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

sql_stmt = "insert into tabmany values(?,?)"
stmt = ibm_db.prepare(conn, sql_stmt)
id = 3
name = "Sam"
ibm_db.bind_param(stmt, 1, id)
ibm_db.bind_param(stmt, 2, name)
try:
    ibm_db.execute(stmt)
except:
    print(ibm_db.stmt_errormsg())
