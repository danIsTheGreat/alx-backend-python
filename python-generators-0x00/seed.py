# Import a mysql driver to connect mysql server with python

import mysql.connector 
import csv

def connect_db():

    """ Connects to the mysql database server running locally. """

    try:

        # Connect with mysql server

        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345"
        )
        
        return connection

    except mysql.connector.Error as error:
    
        print(error)


def create_database(connection):

    """ Creates the database ALX_prodev if the database does not exist. """

    
    try:
        
        # Get cusor to execute sql commands and also fetch results

        cursor = connection.cursor()

        # Run a sql command to create the database

        sql_query = "CREATE DATABASE IF NOT EXISTS ALX_prodev"

        cursor.execute(sql_query)

        # close the cursor

        cursor.close()

    except mysql.connector.Error as error:
        
        print(error)

def connect_to_prodev():

    """ Connects to the ALX_prodev database in MYSQL """
    try:

        # Connect with mysql server

        connection = mysql.connector.connect(
                 host="localhost",
                 user="root",
                 password="12345",
                 database="ALX_prodev"
        )

        print(connection)

        print('connected with ALX_prodev successfully.')
        
        return connection

    except mysql.connector.Error as error:

        print(error)


def create_table(connection):

    """ Creates a table called user_data if it does not exists with the required fileds """

    # SQL query to construct a table user_data 

    sql_query = """

    CREATE TABLE IF NOT EXISTS user_data (

    user_id CHAR(36) PRIMARY KEY DEFAULT (UUID()),
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    age DECIMAL(3,0) NOT NULL
    
    )

    """

    # Get cursor to execute the SQL command to create user_data table

    cursor = connection.cursor()

    # execute the SQL query

    cursor.execute(sql_query)

    # close connection 

    cursor.close()


def insert_data(connection, data):

    """ 
    
    Inserts data in the database ALX_prodev under the table user_data if it does not exist 

    data: a csv file holding all the rows to be inserted 

    """

    cursor = connection.cursor()


    # Open and Read the csv file content. Get a reader object to iterate over the rows.

    user_data = open(data)

    sql_rows = csv.reader(user_data)

    # Iterate over all the rows , except the headers.

    next(sql_rows)

    for row in sql_rows:

        # Construct SQL query & execute

        user_name = row[0]
        user_email = row[1]
        user_age = row[2]

        sql_query = """ 

        INSERT INTO user_data(name, email, age) VALUES(%s, %s , %s)

        """

        cursor.execute(sql_query, (user_name, user_email, user_age))

    connection.commit() # Save changes

    cursor.close()


def get_databases(connection):

    """ Fetch the available databases inside mysql server """
    
    # Construct query

    sql_query = "SHOW DATABASES;"

    # Run the query

    cursor = connection.cursor()

    cursor.execute(sql_query)

    # fetch and print the databases

    print(cursor.fetchall())

def get_user_data(connection):
    
    """ Get all rows from the table user_data """

    sql_query = """ SELECT * FROM user_data """

    cursor = connection.cursor()

    cursor.execute(sql_query)

    rows = cursor.fetchall()

    print(rows)




connection = connect_db()

create_database(connection)

get_databases(connection)

connection = connect_to_prodev()

create_table(connection)

insert_data(connection, 'user_data.csv')

get_user_data(connection)

insert_data(connection, 'user_data.csv')
