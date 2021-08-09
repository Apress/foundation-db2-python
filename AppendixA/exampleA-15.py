import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

stmtOption = {ibm_db.SQL_ATTR_CURSOR_TYPE: ibm_db.SQL_CURSOR_FORWARD_ONLY}
sqlStatement = "SELECT * FROM tabmany"
resultSet = ibm_db.exec_immediate(conn, sqlStatement, stmtOption)

#get the cursor type
cursorType = ibm_db.cursor_type(resultSet)
