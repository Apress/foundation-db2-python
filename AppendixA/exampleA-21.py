import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')

sql = "select id, name from tabmany"
stmt = ibm_db.prepare(conn, sql,{ibm_db.SQL_ATTR_CURSOR_TYPE: ibm_db.SQL_CURSOR_KEYSET_DRIVEN})
result = ibm_db.execute(stmt)
#fetch every alternate row starting from 2nd 
i = 2
row = ibm_db.fetch_assoc(stmt, i)
while ( row ):
    print("%-5d %-16s " % (row['ID'], row['NAME']))
    i = i + 2
    row = ibm_db.fetch_assoc(stmt, i)
