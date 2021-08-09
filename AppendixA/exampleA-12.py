import ibm_db
#use connection string
dbstring = "DATABASE=dbname;HOSTNAME=host;PORT=port;PROTOCOL=TCPIP;UID=username;PWD=password"

#use options
options = {ibm_db.SQL_ATTR_INFO_PROGRAMNAME : 'TestProgram', \
           ibm_db.SQL_ATTR_CURRENT_SCHEMA : 'MYSCHEMA'}
conn=ibm_db.connectdbstring,'','', options)

#Note: Local cataloged database implicit connection

#i) If database parameter specified is a local database alias name with blank userid and #password then connect/pconnect API will use current logged in user's userid for implicit #connection eg: **conn = ibm_db.connect('sample', '', '')**

#ii) If database parameter is a connection string with value "DSN=database_name" then
#connect/pconnect API will use current logged in user's userid for implicit connection
#eg: **conn = ibm_db.connect('DSN=sampledb', '', '')**
#If you are using DSN in connection string as in above example, then you must specify other 
#necessary connection details like hostname, userid, password via supported keywords in 
#db2dsdriver.cfg configuration file located under site-packages/clidriver/cfg or under the cfg 
#folder as per the path you have set IBM_DB_HOME to. You can refer to the sample file below.
#For more information, please refer [IBM data server driver configuration 
#keywords](https://www.ibm.com/support/knowledgecenter/en/SSEPGG_11.1.0/com.ibm.swg.im.dbclient.
#config.doc/doc/c0054698.html).
