import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

create_table = "create table index_test(id int, data VARCHAR(50))"
rc = ibm_db.exec_immediate(conn, create_table)
create_index = "CREATE UNIQUE INDEX index1 ON index_test (id)"
rc = ibm_db.exec_immediate(conn, create_index)

schemaName = "DB2ADMIN"
tableName = "INDEX_TEST"
resultSet = ibm_db.statistics(conn, None, schemaName, tableName, True)
dataRecord = ibm_db.fetch_assoc(resultSet)
while dataRecord['INDEX_NAME'] is not None:
    print("Table Schema            : {}" .format(dataRecord['TABLE_SCHEM']))
    print("Table name              : {}" .format(dataRecord['TABLE_NAME']))
    print("Index qualifier            : {}" .format(dataRecord['INDEX_QUALIFIER']))
    print("Index name                       : {}" .format(dataRecord['INDEX_NAME']))
    print("Column name                      : {}" .format(dataRecord['COLUMN_NAME']))
    print("Column position in index         : {}" .format(dataRecord['ORDINAL_POSITION']))
    dataRecord = ibm_db.fetch_assoc(resultSet)	
