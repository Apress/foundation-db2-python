dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

stmt = ibm_db.exec_immediate(conn,"drop table test_primary_keys")
statement = 'CREATE TABLE test_primary_keys (id INTEGER NOT NULL, PRIMARY KEY(id))'
result = ibm_db.exec_immediate(conn, statement)
stmt = ibm_db.primary_keys(conn, None, None, 'TEST_PRIMARY_KEYS')
row = ibm_db.fetch_tuple(stmt)
print("{} is primary key in table {} with index position {} in the key".format(row[3],row[2],row[4]))
