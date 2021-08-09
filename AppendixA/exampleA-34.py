import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

create_proc = """create procedure multi_results() 
result sets 3
language sql
Begin
DECLARE c1 CURSOR WITH RETURN FOR 
select name, id from tabmany;

DECLARE c2 CURSOR WITH RETURN FOR
select name, id from tabmany where id < 40;

DECLARE c3 CURSOR WITH RETURN FOR
select name, id from tabmany where id > 40;

OPEN c1;
OPEN c2;
OPEN c3;
END """

try:
    rc = ibm_db.exec_immediate(conn, create_proc)
except:
    pass

# retrieve first result set
resultSet_1 = None
try:
    resultSet_1 = ibm_db.callproc(conn, 'multi_results')
except:
    print("stored procedure invocation\n")
    print(ibm_db.stmt_errormsg())
    pass


if resultSet_1:
    row = ibm_db.fetch_tuple(resultSet_1)
    while row:
        for i in row:
            print(i)
        row = ibm_db.fetch_tuple(resultSet_1)

# retrieve second result set
resultSet_2 = None
try:
    resultSet_2 = ibm_db.next_result(resultSet_1)
except Exception:
    pass	

if resultSet_2:
    row = ibm_db.fetch_tuple(resultSet_2)
    while row:
        for i in row:
            print(i)
        row = ibm_db.fetch_tuple(resultSet_2)

# retrieve third result set		
resultSet_3 = None
try:
    resultSet_3 = ibm_db.next_result(resultSet_1)
except Exception:
    pass

if resultSet_3:
    row = ibm_db.fetch_tuple(resultSet_3)
    while row:
        for i in row:
            print(i)
        row = ibm_db.fetch_tuple(resultSet_3)
