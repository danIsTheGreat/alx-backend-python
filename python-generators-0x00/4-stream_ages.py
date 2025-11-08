#!/usr/bin/python3 

seed = __import__('seed')

def yield_ages():

    """ yiled users age one by one from users_data table """

    try:
        # Connects with ALX_prodev table 

        connection = seed.connect_to_prodev()

        cursor = connection.cursor(dictionary=True)

        # Run the query to fetch all users age column from user_data table

        sql_query = """

        SELECT age FROM user_data 

        """

        cursor.execute(sql_query)

        # fetch the age of the first row

        row = cursor.fetchone()

        while row:

            yield row['age']

            row = cursor.fetchone()
    except mysql.connector.Error as error:
        print(error)

    finally:
        cursor.close()
        connection.close()

def stream_user_ages():

    """ Compute the average age of all users in user_data table """

    sum_of_ages = 0 
    counter = 0

    for age in yield_ages():
        sum_of_ages += age
        counter += 1

    # No user insid the table

    if counter == 0:
        return 0 

    average_age_of_users = sum_of_ages / counter

    return average_age_of_users

