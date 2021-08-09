#!/usr/bin/python

import sys, getpass
import ibm_db


# main program
driver = "{IBM DB2 ODBC DRIVER}"  # Db2 driver information
host = '192.168.1.201'            # database host IP or dns address
port = "50000"                    # host port
db = "sample"                     # database registered name
uid = None                        # userid on the database host
pw = None                         # password of the uid
autocommit = ''                   # autocommit default override 
connecttype = ''                  # connect type default override
uid = input("Enter the Db2 userid to be used: ")
pw = getpass.getpass(prompt = "Password for %s: " % uid) 
if pw == None or pw == '': 
    print("The password you entered is incorrect.")
    exit(-1)
conn_str = 'DRIVER=' + driver + ';HOSTNAME=' + host + \
           ';PORT=' + port + ';DATABASE=' + db + \
           ';UID=' + uid + ';PWD=' + pw
connID = ibm_db.connect(conn_str, autocommit, connecttype)
# If the connection fails for any reason an uncaught exception is thrown
# and the program will exit with an error.

# create the sample table
sqlstmt = """CREATE TABLE myexampletable (
    C01        INTEGER NOT NULL
               GENERATED ALWAYS AS IDENTITY
               (START WITH 1, INCREMENT BY 1),
    C02        CHAR(50),
    C03        VARCHAR(70),
    C04        DEC(15,2),
    C05        FLOAT(21),
    C06        CLOB(1K),
    C07        VARGRAPHIC(2000),
    C08        BLOB(1M),
    C09        DATE,
    C10        TIME,
    C11        TIMESTAMP,
    C12        XML,
    C13        BOOLEAN,
    PRIMARY KEY(C01))"""
try:
    rc = ibm_db.exec_immediate(connID, sqlstmt)
except:
    print("Create ' {} ' failed with ".format(sqlstmt))
    print("Error : {}".format(ibm_db.stmt_errormsg()))
    exit(-1)
print('\n    The CREATE statement executed successfully.')

ibm_db.close(connID)
exit(0)

