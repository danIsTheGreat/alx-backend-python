#!/usr/bin/python3

import mysql.connector

seed = __import__('seed')

def lazy_paginate(page_size):

    """ 
    page_size is the number of rows per page.

    calls paginate_user(page_size, offset) and yield the result or rows

    """

    offset = 0 # Initally at 0

    while True:

        rows = paginate_users(page_size, offset)

        if not rows:
            break 

        yield rows

        offset = offset + page_size



def paginate_users(page_size, offset):

    """ fetch and returns rows from table user_data limited by offset """

    connection = seed.connect_to_prodev()
    cursor = connection.cursor(dictionary=True)
    cursor.execute(f"SELECT * FROM user_data LIMIT {page_size} OFFSET {offset}")
    rows = cursor.fetchall()
    connection.close()
    return rows
