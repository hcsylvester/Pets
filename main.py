# Hunter Sylvester
# Purpose: Shows all pets from an SQL database and lets people look at the info pertaining to that specific email
#
# We need to install the mypysql library
# In the Terminal window (bottom of PyCharm), run
# pip3 install pymysql
# pip3 install cryptography

# Import pet class, module, and cred file for MySQL access
from petsClass import Pets
import pymysql.cursors
from creds import *

# Create a pet list that is empty for later use
petList = []

# Function that accesses sql pets data and inputs data into Pets class
def gatherData():
    # sql statement
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

    # Loop through the specific sql statement reading data into petList for each row
    for row in cursor:
        variable = Pets(petName=row['pets_name'],
                        ownerName=row['owners_name'],
                        petAge=row['age'],
                        animalType=row['animal_type'],
                        animalId=row['id'])
        petList.append(variable)

# Connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"Sorry, connection was not made to sql database.  Check mysql information is set correctly.")
    print()
    exit()

# Once connected, we execute a query
try:
    with myConnection.cursor() as cursor:
        # ==================
        # Runs the function to access sql with specific sql commands and gives the Pets data
        gatherData()

# If there is an exception
except Exception as e:
    print(f"Sorry, but the connection was not made. Check mysql information.")
    print()

# Close connection
finally:
    myConnection.close()
    print("Connection closed.")
    print("\n")

# Show the list of pets to person and let them choose one until they want to quit
while True:
    try:
        print("Please choose a pet from the list below:")

        # Prints each pet with id
        for i in petList:
            print(f"[{i.getAnimalId()}]  {i.getPetName()}")

        print("[Q] Quit")

        requestAnimal = input('Please enter a pet ID (integer) to see more info pertaining to that pet '
                              'or press [Q] to quit! \n')

        if str.upper(requestAnimal) == "Q":
            print("Thank you and have a nice day!")
            break

        elif 1 <= int(requestAnimal) <= 8 or int(requestAnimal) == 10:
            if int(requestAnimal) == 10:
                # Must subtract 2 due to the indexing of Rex
                value = petList[int(requestAnimal)-2]
                print(f"{value.getPetName()} is {value.getPetAge()} years old.  "
                      f"{value.getPetName()} is a {value.getAnimalType()}.  "
                      f"{value.getPetName()}'s owner is {value.getOwnerName()}.")
                input("Press [ENTER] to continue! \n")

            else:
                # Must subtract 1 due to the index starting at 0
                value = petList[int(requestAnimal)-1]
                print(f"{value.getPetName()} is {value.getPetAge()} years old.  "
                      f"{value.getPetName()} is a {value.getAnimalType()}.  "
                      f"{value.getPetName()}'s owner is {value.getOwnerName()}. \n")
                input("Press [ENTER] to continue! \n")

        else:
            input(f'{requestAnimal} is not associated with one of the pets. \nPlease press [ENTER] to continue! \n')

    except Exception:
        print(f'{requestAnimal} is not associated with one of the pets.  Remember, it must be one of their IDs or "Q" '
              f'to quit!')
        input("Press [ENTER] to continue!\n")
