#!/usr/bin/python

import sys, getpass
import ibm_db


def getColNamesWidths(results):
    # get the width of each column
    columns = list()
    col = 0
    numColumns = 0
    try:
        numColumns = ibm_db.num_fields(results)
    except Exception:
        pass
    # If information about the number columns returned could not be obtained, 
    # display an error message and exit .
    if numColumns is False:
        print("\nERROR: Unable to obtain information about the result set produced.")
        conn.closeConnection()
        exit(-1)
    while col < numColumns:
        col_name = ibm_db.field_name(results, col)
        col_width = ibm_db.field_width(results, col)
        # the field name can be bigger than the display width
        col_width = max(len(col_name), col_width)
        columns.append((col_name, col_width))
        col += 1
    return columns # return a list of tuples (name, size)

def populateColTitleLines(columns):
    # populate the two title lines for the results
    col = 0
    line = ''
    lines = []
    # do the title line
    while col < len(columns):
        (col_name, col_width) = columns[col]
        title = col_name + ((col_width - len(col_name)) * ' ')
        line += '  ' + title
        col += 1
    lines.append(line)
    # do the underlines
    col = 0
    line = ''
    while col < len(columns):
        (col_name, col_width) = columns[col]
        line += '  ' + (col_width * '-')
        col += 1
    lines.append(line)
    return lines # return the two title lines

def populateLines(results, headerLines):
    # get the data records
    lines = []
    record = ibm_db.fetch_tuple(results)
    while record is not False:
        line = ''
        col = 0
        numColumns = 0
        try:
            numColumns = ibm_db.num_fields(results)
        except Exception:
            pass
        # If information about the number columns returned could not be obtained, 
        # display an error message and exit .
        if numColumns is False:
            print("\nERROR: Unable to obtain information about the result set produced.")
            conn.closeConnection()
            exit(-1)
        while col < numColumns:
            colstr = record[col]
            (name, col_width) = headerLines[col]
            coltype = ibm_db.field_type(results, col)
            if record[col] is None:
                line += '  -' + ((col_width - 1) * ' ')
            elif coltype in ("clob", "dbclob", "blob", "xml", "string"):
                # these are the string types
                line += '  ' + str(colstr) + ((col_width - len(colstr)) * ' ')
            else:
                # these are the numeric types, or at least close enough
                colstr = str(colstr)
                line += '  ' + ((col_width - len(colstr)) * ' ') + colstr
            col += 1
        lines.append(line)
        record = ibm_db.fetch_tuple(results)
    return lines


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

# get the records from the database
sqlstmt = """SELECT e.empno, e.lastname, d.deptname FROM emp e 
    INNER JOIN dept d ON e.workdept = d.deptno AND d.deptname = ?"""
prepstmt = ibm_db.prepare(connID, sqlstmt)
if prepstmt is False:
    print("Unable to prepare the statement.")
    exit(-1)
deptnme = 'SOFTWARE SUPPORT'
retcode = ibm_db.bind_param(prepstmt, 1, deptnme, ibm_db.SQL_PARAM_INPUT, \
                            ibm_db.SQL_CHAR)
results = ibm_db.execute(prepstmt)
headerLines = getColNamesWidths(prepstmt)
titleLines = populateColTitleLines(headerLines)
dataLines = populateLines(prepstmt, headerLines)
selrecords = len(dataLines)

#print the result lines
for line in titleLines:
    print(line)
for line in dataLines:
    print(line)
# print the number of records returned
print('\n    ' + str(selrecords) + ' record(s) selected.')

ibm_db.close(connID)
exit(0)

