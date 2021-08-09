import ibm_db

#try connecting with an invalid user name
try:
    dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=uname;PWD=password"
    conn=ibm_db.connect(dbstring, '', '', '')
except:
    print("Error in connection, sqlstate = ")
    errorState = ibm_db.conn_error()
    print(errorState)
