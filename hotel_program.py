"""
A hotel has 400 rooms (100-499), spread evenly among four floors, 
where the first number of the room corresponds to the floor (e.g. 
room 305 is on the third floor). Rooms have different features 
depending on the room number: • Master suites are every twenty-fifth room on a floor. Master suites have one king-sized bed. 
• All odd-numbered rooms, except for master suites, 
have one queen-sized bed. • All even-numbered rooms, except for 
master suites, have two twin-sized beds. • Every tenth room, with 
the exception of those on the first floor, has a balcony. Given a 
room number entered by the user, determine the floor number, the 
types of beds in the room and whether or not it has a balcony.
For example, room 295 has one queen-sized bed, while room 450 is
a master suite with a king-sized bed and a balcony. If the room
number is not valid, output the message "Not a valid number".
"""

query = input("Enter room number:\n")
# query = 450
def roomInfo():

    if int(query) % 25 == 0:
        print("Master suite, King size bed")
    elif int(query) % 2 != 0 and int(query) % 25 != 0:    
        print("Odd number, Queen size bed")
    elif int(query) % 2 == 0:
        print("Even number, Two Twin size beds")
    else:
        print("Unknown")

if int(query) >= 100 and int(query) < 200:
    print("First floor")
    roomInfo()

elif int(query) >= 200 and int(query) < 300:
    print("Second floor")
    roomInfo()

elif int(query) >= 300 and int(query) < 400:
    print("Third floor")
    roomInfo()

elif int(query) >= 400 and int(query) < 500:
    print("Fourth floor")
    roomInfo()
else:
    print("Not a valid number.")
    quit

# if room > 100 < 500 and div by 10 has blacony
if int(query) >= 200 and int(query) < 500 and int(query) % 10 == 0:
    print("Has balcony")