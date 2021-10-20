# Ken Holm
# Purpose: This is my CRUD test program
# Create
# Read
# Update
# Delete
#
# See https://pymysql.readthedocs.io/en/latest/index.html
#  We need to install the mypysql library
#  In the Terminal window (bottom of PyCharm), run
#  pip3 install pymysql
# pip3 install cryptography

from petsClass import Pets
import pymysql.cursors
from creds import *

petList = []

def showData():
    # Our sql statement, easy to read
    sqlSelect = """
      Select pets.name as pets_name, pets.age, owners.name as owners_name, types.animal_type from pets join owners on 
      pets.owner_id = owners.id join types on pets.animal_type_id = types.id;
      
      """

    # Execute select
    cursor.execute(sqlSelect)

    # Loop through all the results
    #  Print the data, nicely
    for row in cursor:
        print(row)

        variable = Pets(petName = row['petName'],
                             ownerName=row['ownerName'],
                             petAge=row['petAge'],
                             animalType=row['animalType'],
                             animalId=row['animalId'])
        petList.append(variable)
        print(variable)
    input("Press [ENTER] to continue. ")

# def listData():
#     # Our sql statement, easy to read
#     sqlSelect = """
#       Select pets.name as pets_name, pets.age, owners.name as owners_name, types.animal_type from pets join owners on
#       pets.owner_id = owners.id join types on pets.animal_type_id = types.id;
#
#       """
#
#     # Execute select
#     cursor.execute(sqlSelect)
#     # Loop through all the results
#     #  Print the data, nicely
#     for row in cursor:
#         variable = Pets(petName = row['petName'],
#                         ownerName=row['ownerName'],
#                         petAge=row['petAge'],
#                         animalType=row['animalType'],
#                         animalId=row['animalId'])
#         petList.append(variable)
#     print(petList)

#Now we create an object for each one of these animals
# Connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()
    exit()


# Now that we are connected, execute a query
#  and do something with the result set.
try:
    with myConnection.cursor() as cursor:
        # ==================
        # Show initial data
        print(f"These are all of the animals and their owners!")
        showData()
    #     variable = []
    #     for row in cursor:
    #         variable = Pets(row['petName'],
    #                         row['ownerName'],
    #                         row['petAge'],
    #                         row['animalType'],
    #                         row['animalId'])
    #     petList.append(variable)
    #
    # print(petList)

        # # NOTE: We are using placeholders in our SQL statement
        # #  See https://dev.mysql.com/doc/connector-python/en/connector-python-api-mysqlcursor-execute.html
        # sqlInsert = """
        #     insert into
        #       pets (id, first_name, last_name, username)
        #     values
        #       (%s, %s, %s, %s);
        #     """
        #
        # sqlUpdate = """
        #     update
        #       pets
        #     set
        #       first_name = %s
        #     where
        #       id = %s;
        #     """
        #
        # sqlDelete = """
        #     delete from
        #       pets
        #     where
        #       id = %s;
        #     """
        # # ===============
        # # Execute insert
        # print(f"Inserting data")
        # cursor.execute(sqlInsert, (9999, 'Ken', 'Holm', 'kholm'))
        #
        # print(f"We have executed the INSERT statement")
        # print(f"Does the data exist outside of this program?")
        # showData()
        #
        # # Now, we have to COMMIT our command
        # myConnection.commit()
        #
        # print(f"We have now committed the data")
        # print(f"What about now?")
        # showData()
        #
        # # ===============
        # # Execute update
        # print(f"Updating data")
        # cursor.execute(sqlUpdate, ('Alex', 9999))
        #
        # # Now, we have to COMMIT our command
        # myConnection.commit()
        #
        # showData()
        #
        # # ===============
        # # Execute delete
        # print(f"Delete data")
        # cursor.execute(sqlDelete, (9999))
        #
        # # Now, we have to COMMIT our command
        # myConnection.commit()
        #
        # showData()


# If there is an exception, show what that is
except Exception as e:
    print(f"An error has occurred.  Exiting: {e}")
    print()

# Close connection
finally:
    myConnection.close()
    print("Connection closed.")



