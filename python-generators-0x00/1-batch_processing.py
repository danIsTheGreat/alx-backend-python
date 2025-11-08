#!/usr/bin/python3

import mysql.connector

def stream_users_in_batches(batch_size):

    """ Fetchs rows from table user_data in batch size specifided in batch_size """
    try:

        connection = mysql.connector.connect(
        
                host="localhost",
                user="root",
                password="12345",
                database="ALX_prodev"
        )

        cursor = connection.cursor(dictionary=True)

        # SQL query to fecth rows. number of rows matchs batch_size

        sql_query = """

        SELECT * FROM user_data LIMIT %s

        """

        # execute the sql query

        cursor.execute(sql_query, (batch_size,))

        # first row in user_data table

        row = cursor.fetchone()

        # Generator returns 1 row at a time

        while row:

            yield row

            row = cursor.fetchone()
    
    except mysql.connector.Error as error:
    
        print(error)

    finally:
        
        cursor.close()
        connection.close()

def batch_processing(batch_size):
    
    """ Process batch of sql rows and filter users over the age of 25 """

    stream_user_data = stream_users_in_batches(batch_size)

    for user in stream_user_data:
        if (user['age']) > 25:
            print(user)

