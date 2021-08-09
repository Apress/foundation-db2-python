#!/usr/bin/python

import sys, getpass
import ibm_db


# main program
resultSet = False
dataRecord = False
tableName = "EMP"
sqlDataTypes = {0 : "SQL_UNKNOWN_TYPE", 1 : "SQL_CHAR", 2 : "SQL_NUMERIC", 3 : "SQL_DECIMAL",
    4 : "SQL_INTEGER", 5 : "SQL_SMALLINT", 6 : "SQL_FLOAT", 7 : "SQL_REAL", 8 : "SQL_DOUBLE",
    9 : "SQL_DATETIME", 12 : "SQL_VARCHAR", 16 : "SQL_BOOLEAN", 19 : "SQL_ROW", 
   91 : "SQL_TYPE_DATE", 92 : "SQL_TYPE_TIME", 93 : "SQL_TYPE_TIMESTAMP",
   95 : "SQL_TYPE_TIMESTAMP_WITH_TIMEZONE", -8 : "SQL_WCHAR", -9 : "SQL_WVARCHAR",
  -10 : "SQL_WLONGVARCHAR", -95 : "SQL_GRAPHIC", -96 : "SQL_VARGRAPHIC",
  -97 : "SQL_LONGVARGRAPHIC", -98 : "SQL_BLOB", -99 : "SQL_CLOB", -350 : "SQL_DBCLOB",
 -360 : "SQL_DECFLOAT", -370 : "SQL_XML", -380 : "SQL_CURSORHANDLE", -400 : "SQL_DATALINK",
 -450 : "SQL_USER_DEFINED_TYPE"}
sqlDateTimeSubtypes = {1 : "SQL_CODE_DATE", 2 : "SQL_CODE_TIME", 3 : "SQL_CODE_TIMESTAMP",
    4 : "SQL_CODE_TIMESTAMP_WITH_TIMEZONE"}
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
connID = ibm_db.connect(conn_str, '', '')
# If the connection fails for any reason an uncaught exception is thrown
# and the program will exit with an error.

# Attempt to retrieve information about all columns of a table
resultSet = ibm_db.columns(connID, None, None, tableName, None)
# If The Information Desired Could Not Be Retrieved, Display An Error Message And Exit
if resultSet is False:
    print("\nERROR: Unable to obtain the information desired\n.")
    conn.closeConnection()
    exit(-1)
noData = False
loopCounter = 1
while noData is False:
    dataRecord = ibm_db.fetch_assoc(resultSet)
    if dataRecord is False:
        noData = True
    else:
        # Display Record Header Information
        print("Column " + str(loopCounter) + " details:")
        print("_________________________________________")
        # Display The Information Stored In The Data Record Retrieved
        print("Table schema             : {}" .format(dataRecord['TABLE_SCHEM']))
        print("Table name               : {}" .format(dataRecord['TABLE_NAME']))
        print("Column name              : {}" .format(dataRecord['COLUMN_NAME']))
        print("Data type                : {}" .format(dataRecord['TYPE_NAME']))
        print("Size                     : {}" .format(dataRecord['COLUMN_SIZE']))
        print("Buffer size              : {}" .format(dataRecord['BUFFER_LENGTH']))
        print("Scale (decimal digits)   : ", end="")
        if dataRecord['DECIMAL_DIGITS'] == None:
            print("Not applicable")
        else:
            print("{}" .format(dataRecord['DECIMAL_DIGITS']))
        print("Precision radix          : ", end="")
        if dataRecord['NUM_PREC_RADIX'] == 10:
            print("Exact numeric data type")
        elif dataRecord['NUM_PREC_RADIX'] == 2:
            print("Approximate numeric data type")
        elif dataRecord['NUM_PREC_RADIX'] == None:
            print("Not applicable")
        print("Can accept NULL values   : ", end="")
        if dataRecord['NULLABLE'] == ibm_db.SQL_FALSE:
            print("NO")
        elif dataRecord['NULLABLE'] == ibm_db.SQL_TRUE:
            print("YES")
        print("Remarks                  : {}" .format(dataRecord['REMARKS']))
        print("Default value            : {}" .format(dataRecord['COLUMN_DEF']))
        print("SQL data type            : ", end="")
        print(sqlDataTypes.get(dataRecord['SQL_DATA_TYPE']))
        print("SQL data/time subtype    : ", end="")
        print(sqlDateTimeSubtypes.get(dataRecord['SQL_DATETIME_SUB']))
        print("Data type                : {}" .format(dataRecord['DATA_TYPE']))
        print("Length in octets         : ", end="")
        if dataRecord['CHAR_OCTET_LENGTH'] == None:
            print("Not applicable")
        else:
            print("{}" .format(dataRecord['CHAR_OCTET_LENGTH']))
        print("Ordinal position         : {}" .format(dataRecord['ORDINAL_POSITION']))
        print("Can contain NULL values  : {}" .format(dataRecord['IS_NULLABLE']))

        # Increment The loopCounter Variable And Print A Blank Line To Separate The
        # Records From Each Other
        loopCounter += 1
        print()

ibm_db.close(connID)
exit(0)

