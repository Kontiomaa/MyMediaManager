from files.db import initdb
from files.db import dumpDatabaseContent
from files.listMedia import listOptions
from files.searchMedia import searchOptions

initdb()

print('What do you want to do?')
print('1. List')
print('2. Search')
print('3. Insert')
print('4. Delete')
print('5. Backup')
print('6. Quit')

isCorrectNum = False

while not isCorrectNum:
    try:
        userinput = None
        userinput = int(input())
        if 0 < userinput < 7:
            isCorrectNum = True
        else:
            print('Else route:', userinput)
            print('Enter a number (1-6)')
    except ValueError:
        print('Value error:', userinput)
        print('Enter a number (1-6)')

if userinput == 1:
    listOptions()
elif userinput == 2:
    searchOptions()
elif userinput == 3:
    print('Insert')
elif userinput == 4:
    print('Delete')
elif userinput == 5:
    print('Backup')
elif userinput == 6:
    print('Quit')
else:
    print('Enter a number (1-5)')
