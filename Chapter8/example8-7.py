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

# Test if the connection is active
active = ibm_db.active(connID)
if active:
    print('The currect connection is active.')
else:
    print('*The current connection is not active.')
# Test autocommit 
commit = ibm_db.autocommit(connID)
if active:
    print('Autocommit is active.')
else:
    print('*Autocommit is not active.')
# Get the client info
clientinfo = ibm_db.client_info(connID)
if clientinfo:
    print('Client info:')
    print('  APPL_CODEPAGE: ', clientinfo.APPL_CODEPAGE)
    print('  CONN_CODEPAGE: ', clientinfo.CONN_CODEPAGE)
    print('  DATA_SOURCE_NAME: ', clientinfo.DATA_SOURCE_NAME)
    print('  DRIVER_NAME: ', clientinfo.DRIVER_NAME)
    print('  DRIVER_ODBC_VER: ', clientinfo.DRIVER_ODBC_VER)
    print('  DRIVER_VER: ', clientinfo.DRIVER_VER)
    print('  ODBC_SQL_CONFORMANCE: ', clientinfo.ODBC_SQL_CONFORMANCE)
    print('  ODBC_VER: ', clientinfo.ODBC_VER)
else:
    print('Could not obtain client info.')
# Get column priviliges, if they exist
priv = ibm_db.column_privileges(connID, None, uid.upper(), 'employee', 'workdept')
row = ibm_db.fetch_assoc(priv)
if row:
    print('Sample database, table department, column priviliges:')
    print("  Schema name            : {}" .format(row['TABLE_SCHEM']))
    print("  Table name             : {}" .format(row['TABLE_NAME']))
    print("  Column name            : {}" .format(row['COLUMN_NAME']))
    print("  Privilege grantor      : {}" .format(row['GRANTOR']))
    print("  Privilege recipient    : {}" .format(row['GRANTEE']))
    print("  Privilege              : {}" .format(row['PRIVILEGE']))
    print("  Privilege is grantable : {}" .format(row['IS_GRANTABLE'])) 
else:
    print('No column privileges to retrieve.')
# Get column metadata, if it exists
coldata = ibm_db.columns(connID, None, None, 'employee', 'empno')
row = ibm_db.fetch_assoc(coldata)
if row:
    print('Sample database, table department, columns metadata:')
    table_name = row['TABLE_NAME']
    column_name = row['COLUMN_NAME'] 
    print("  Table name   : {}" .format(table_name))
    print("    Column name  : {}" .format(column_name))
else:
    print('No column metadata to retrieve.')
# Test SQL commit
rc = ibm_db.commit(connID)
if rc:
    print('Commit succeeded.')
else:
    print('*Commit did not succeed.')

ibm_db.close(connID)
exit(0)

