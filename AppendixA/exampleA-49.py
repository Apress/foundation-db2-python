import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

create_table = "create table index_test(id int, data VARCHAR(50)"
try:
    rc = ibm_db.exec_immediate(conn, create_table)
except:
    print("Query ' {} ' failed with ".format(create_table))
    print("SQLSTATE = {}".format(ibm_db.stmt_error()))
