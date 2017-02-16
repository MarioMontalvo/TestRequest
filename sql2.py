import MySQLdb
 
DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_PASS = 'mysqlroot' 
DB_NAME = 'a' 
 
def run_query(query=''):
	
	datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
	