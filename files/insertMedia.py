from files.db import insertToDatabase

def newData():
    print("Need objects to get this working properly")

    dboptions = [['category','c_name'], ['tag','t_name']]

    print("What would you like to add?\n")
    print("1. A category")
    print("2. A tag")
    #print("3. An artist")
    #print("4. Media")

    while True:
        try:
            userinput = None
            userinput = int(input())
            if 0 < userinput < 3:
                print('Enter new ' + dboptions[userinput-1][0] + ' name:')
                userNewData = str(input())
                insertToDatabase(dboptions[userinput-1], userNewData)
                break
            else:
                print('Enter a number (1-2)')
        except ValueError:
            print('Enter a number (1-2)')
