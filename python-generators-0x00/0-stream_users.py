#!/usr/bin/python3

import mysql.connector

def stream_users():

    """ 
    a generator function that returns 1 row at a time without loading all the rows at once in memory
    
    """

    connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="12345",
            database="ALX_prodev"
            )

    cursor = connection.cursor(dictionary=True)

    sql_query = """

    SELECT * FROM user_data 

    """

    # Excute the SQL query 

    cursor.execute(sql_query)

    # Iterate over and fetch the rows inside user_data

    row = cursor.fetchone() # Get the first row value

    while row:

        yield row # Fetch and send back a single row
        
        row = cursor.fetchone() # Fetch a single row from the user_data table

    cursor.close()
    connection.close()

