import ibm_db
import ibm_db_dbi as dbi
import pandas as pd

dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn = ibm_db.connect(dbstring, '', '', '')

ibm_db.exec_immediate(conn,"CREATE table tabmany( id SMALLINT , name VARCHAR(32))")
insert = "insert into tabmany values(?,?)"
values=(1,'sample')
params=tuple(tuple (x+i if type(x)==int else x+str(i) for x in values) for i in range(3))
stmt_insert = ibm_db.prepare(conn, insert)
ibm_db.execute_many(stmt_insert,params)
row_count = ibm_db.num_rows(stmt_insert)
print("inserted {} rows".format(row_count))

# use data frame, requires ibm_db_dbi connection
dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"
conn1 = ibm_db.connect(dbstring, '', '', '')

data={'ID':[11,22,33,44],'NAME':['val1','val2','val3','val4']}
df1=pd.DataFrame(data)
tuple_of_tuples = tuple([tuple(x) for x in df1.values])
sql="insert into testmany values(?,?)"

stmt=ibm_db.prepare(conn,sql)
ibm_db.execute_many(stmt,tuple_of_tuples)

df2=pd.read_sql("select * from test",conn1) 
print(df2)

subset = df2[['ID','NAME','RATING']]
tuple_of_tuples1 = tuple([tuple(x) for x in subset.values])
ibm_db.execute_many(stmt,tuple_of_tuples1)

df3=pd.read_sql("select * from test", conn1)
print(df3)
