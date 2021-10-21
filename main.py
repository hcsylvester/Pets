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
import pprint as pp
petList = []

def showData():
    # Our sql statement, easy to read
    sqlSelect = """
      Select 
      pets.id as id, 
      pets.name as pets_name, 
      pets.age, 
      owners.name as owners_name, 
      types.animal_type from pets 
      join owners on pets.owner_id = owners.id 
      join types on pets.animal_type_id = types.id;
      
      """

    # Execute select
    cursor.execute(sqlSelect)

    # Loop through all the results
    #  Print the data, nicely
    for row in cursor:
        print(row)

        variable = Pets(petName=row['pets_name'],
                        ownerName=row['owners_name'],
                        petAge=row['age'],
                        animalType=row['animal_type'],
                        animalId=row['id'])
        petList.append(variable)
        
    input("Press [ENTER] to continue. ")


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


        # for row in petList:
        #     variable = []
        pp.pprint(petList)


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

# while True:
#     request = input('Please enter an animal ID to see more info on that animal or press "q" to quit!')
#
#
#     if request == "q":
#         print("Thank you and have a nice day!")
#         break



