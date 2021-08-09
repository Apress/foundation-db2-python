import ibm_db

# Open normal connection
dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')
print("Normal connection 1 = {}".format(conn1))
# Open persistent connections
pconn1 = ibm_db.pconnect('DATABASE=database;HOSTNAME=hostname;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password','','')
print("Persistent connection 1 = {}".format(pconn1))
# pconn2 is same as pconn1
pconn2 = ibm_db.pconnect('DATABASE=database;HOSTNAME=hostname;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password','','')
print("Persistent connection 2 = {}".format(pconn2))

# closing normal connection
ibm_db.close(conn1)
print("Normal connection 1 = {} closed".format(conn1))
# closing persistent connection will not shut off the db connection
ibm_db.close(pconn1)
print("Persistent connection 1 = {} closed".format(pconn1))

# select from the persistent connection
sql = "select * from tabmany"
stmt = ibm_db.exec_immediate(pconn2,sql)

# fetching data from a closed connection results in error
try:
    sql = "select * from tabmany"
    stmt = ibm_db.exec_immediate(conn1,sql)
except:
    print("Connection is closed, Hence can't execute {} on conn1".format(sql))
    pass
