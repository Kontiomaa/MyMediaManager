from files.db import insertToDatabase

def newData():
    print("Todo")

    print("What would you like to add?\n")
    print("1. A category")
    print("2. A tag")
    print("3. An artist")
    print("4. Media")

    while True:
        try:
            userinput = None
            userinput = int(input())
            if 0 < userinput < 5:
                insertToDatabase()
                break
            else:
                print('Enter a number (1-4)')
        except ValueError:
            print('Enter a number (1-4)')
