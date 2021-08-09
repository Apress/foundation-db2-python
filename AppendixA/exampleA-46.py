import ibm_db

conn_options = { ibm_db.SQL_ATTR_INFO_PROGRAMNAME : 'TestProgram'}
dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', conn_options)

value = ibm_db.get_option(conn, ibm_db.SQL_ATTR_INFO_PROGRAMNAME, 1)
print("Connection options:\nSQL_ATTR_INFO_PROGRAMNAME = {}".format(value), end="\n")
returncode = ibm_db.set_option(conn, {ibm_db.SQL_ATTR_AUTOCOMMIT:0},1)
value = ibm_db.get_option(conn, ibm_db.SQL_ATTR_AUTOCOMMIT, 1)
print("SQL_ATTR_AUTOCOMMIT = {}".format(str(value)), end="\n")

# statement options
stmt = ibm_db.prepare(conn, "select * from tabmany")
returnCode = ibm_db.set_option(stmt, {ibm_db.SQL_ATTR_QUERY_TIMEOUT : 20}, 0)
value = ibm_db.get_option(stmt, ibm_db.SQL_ATTR_QUERY_TIMEOUT, 0)
print("Statement options:\nSQL_ATTR_QUERY_TIMEOUT = {}".format(str(value)), end="\n")
result = ibm_db.execute(stmt)

if result:
    ibm_db.free_result(stmt)
else:
    print(ibm_db..stmt_errormsg())
ibm_db.rollback(conn)
ibm_db.close(conn)
