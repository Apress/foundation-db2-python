mport ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn=ibm_db.connect(dbstring, '', '', '')

# ANIMAL is the table name
stmt = ibm_db.column_privileges(conn, None, None, 'ANIMALS')
row = ibm_db.fetch_tuple(stmt)
if row:
    print(row[0])
    print(row[1])
    print(row[2])
    print(row[3])
    print(row[4])
    print(row[5])
    print(row[6])
    print(row[7])

ibm_db.close(conn)
