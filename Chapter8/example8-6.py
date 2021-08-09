#!/usr/bin/python

import sys, getpass
from decimal import *
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

# Add new designer employees to the employee table
sql = """INSERT INTO employee (empno, firstnme, midinit, lastname, 
         workdept, phoneno, hiredate, job, edlevel, sex, birthdate, 
         salary, bonus, comm) VALUES 
         (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
stmt = ibm_db.prepare(connID, sql)
if stmt is False:
    print("Unable to prepare the SQL statement.")
    exit(-1)
emp = ('000350', 'DAVID', 'W', 'ANDREWS', 'D11', '3634', '1969-03-20',  \
    'DESIGNER', 20, 'M', '1951-06-14', 40160.00,  500, 2220)
result = ibm_db.execute(stmt, emp)
if result is False:
    print("Unable to execute the SQL statement.")
    ibm_db.close(connID)
    exit(-1)
# Now update the salary
sql = "UPDATE employee SET salary = ? where empno = '000350'"
stmt = ibm_db.prepare(connID, sql)
if stmt is False:
    print("Unable to prepare the SQL statement.")
    exit(-1)
salary = str(Decimal('40160.00') * Decimal('1.1'))
retcode = ibm_db.bind_param(stmt, 1, salary, ibm_db.SQL_PARAM_INPUT, \
                            ibm_db.SQL_CHAR)
result = ibm_db.execute(stmt)
if result is False:
    print("Unable to execute the SQL statement.")
    ibm_db.close(connID)
    exit(-1)
# Ensure the salary is updated
sql = "select empno, salary from employee where empno = '000350'"
results = ibm_db.exec_immediate(connID, sql)
if results is False:
    print("\nERROR: Unable to execute the SQL statement specified.")
    ibm_db.close(connID)
    exit(-1)
(empno, salary) = ibm_db.fetch_tuple(results)
print('empno: ', str(empno), '  old salary: 40160.00  new salary: ', str(salary))
# Now delete the employee we added
ibm_db.exec_immediate(connID, "delete from employee where empno = '000350'")

ibm_db.close(connID)
exit(0)

