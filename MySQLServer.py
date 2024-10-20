import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
	try:
		cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
		print("Database 'alx_book_store' created successfully!")
	except mysql.connector.Error as err:
	    print(f"Failed creating database: {err}")

def main():
    try: 
    	# connect to MySQL server
        connection = mysql.connector.connect(
        	host= 'local',
        	user= 'root',
        	password= 'Y@obamfo*mysqlDB$$'
        )
        cursor = connection.cursor()

        #Ctreate database
        create_database(cursor)

        #Close cursor and connection
        cursor.close()
        connection.close()

if __name__ == "__main__":
	main()