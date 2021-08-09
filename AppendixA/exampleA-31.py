import ibm_db

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

tkey = "create table test_key(name VARCHAR(30) NOT NULL, idf INTEGER NOT NULL)"
try:
    result = ibm_db.exec_immediate(conn, tkey)
except:
    pass
	
fktable = "create table foreign_key(namef VARCHAR(30) NOT NULL, id INTEGER NOT NULL, FOREIGN KEY(namef) REFERENCES test_keys(name))"
try:
    result = ibm_db.exec_immediate(conn, fktable)
except:
    pass

stmt = ibm_db.foreign_keys(conn, None, None, None, None, None,'FOREIGN_KEY')
row = ibm_db.fetch_tuple(stmt)
print(row[7],"is a foreign key in", row[6], "referencing", row[3], "in table", row[2])
