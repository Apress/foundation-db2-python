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

# Add new designer employees to the employee table
sql = """INSERT INTO employee (empno, firstnme, midinit, lastname, 
         workdept, phoneno, hiredate, job, edlevel, sex, birthdate, 
         salary, bonus, comm) VALUES 
         (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""
stmt = ibm_db.prepare(connID, sql)
if stmt:
    inserts = 0
    with open('./example8-5.csv') as f:
        line = f.readline()
        while len(line) > 0:
            emp_list = line.split(',')
            for i in range(0, len(emp_list)):
                emp_list[i] = emp_list[i].rstrip("' \n")
                emp_list[i] = emp_list[i].lstrip("' ")
            emp = tuple(emp_list)
            result = ibm_db.execute(stmt, emp)
            if result is False:
                print("Unable to execute the SQL statement.")
                exit(-1)
            inserts += 1
            line = f.readline()
    print(str(inserts) + ' employees inserted successfully.')
# Now delete those new employees
ibm_db.exec_immediate(connID, "delete from employee where empno = '000350'")
ibm_db.exec_immediate(connID, "delete from employee where empno = '000360'")
ibm_db.exec_immediate(connID, "delete from employee where empno = '000370'")
ibm_db.exec_immediate(connID, "delete from employee where empno = '000380'")
print('4 employees deleted successfully.')

ibm_db.close(connID)
exit(0)

