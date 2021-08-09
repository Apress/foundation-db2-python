#!/usr/bin/python

import sys, getpass
import ibm_db_dbi

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
#host = host + ':' + port
conn_str = 'DRIVER=' + driver + ';HOSTNAME=' + host + \
           ';PORT=' + port + ';DATABASE=' + db + \
           ';UID=' + uid + ';PWD=' + pw
connID = ibm_db_dbi.connect(dsn=conn_str, conn_options=None)
# If the connection fails for any reason an uncaught exception is thrown
# and the program will exit with an error.

# get a cursor
cursor = connID.cursor()

sqlstmt = 'SELECT projname, deptno FROM project WHERE deptno = ? OR deptno = ?'
cursor.execute(sqlstmt, ('B01', 'D01'))
# build/print header lines and fetch/print all rows
row = cursor.fetchone()
if row:
    rows = 0
    cols = len(cursor.description)
    col = 0
    typecode = []
    collen = []
    tline1 = ''
    tline2 = ''
    i = 0
    # print the report header lines
    while i < cols:
        (name,type_code,display_size,internal_size,precision,scale,null_ok) = \
         cursor.description[i]
        typecode.append(type_code)
        collen.append(max(display_size, len(name)))
        tline1 = tline1 + '  ' + name +  (collen[i]-len(name))*' '
        tline2 = tline2 + '  ' + (collen[i]*'-')
        i += 1
    print(tline1 + '\n' + tline2)
    # print each fetched row
    while row:
        rows += 1
        colvals = list(row)
        i = 0
        line = ''
        while i < cols:
            (name,type_code,display_size,internal_size,precision,scale,null_ok) = \
             cursor.description[i]
            if colvals[i] is None:
                line = line + '  -' + (collen[i]-1)*' '
            elif typecode[i] in ibm_db_dbi.DECIMAL:
                line = line + '  ' + (collen[i]-len(colvals[i]))*' ' + colvals[i]
            else:
                line = line + '  ' + colvals[i] + (collen[i]-len(colvals[i]))*' ' 
            i += 1
        print(line)
        row = cursor.fetchone()
    # print summary
    print('\n    ' + str(rows) + ' record(s) selected.')

connID.close()
exit(0)

