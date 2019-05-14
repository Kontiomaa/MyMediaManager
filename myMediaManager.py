from files.db import initdb
from files.listMedia import listOptions

initdb()

print('What do you want to do?')
print('1. List')
print('2. Search')
print('3. Insert')
print('4. Delete')
print('5. Quit')

isCorrectNum = False

while not isCorrectNum:
    try:
        userinput = None
        userinput = int(input())
        print('assigned: ', userinput)
        #if userinput < 6 & userinput > 0: # Why is this not working properly?
        if 0 < userinput < 6:
            isCorrectNum = True
            print('if route: ', userinput)
        else:
            print('Else route:', userinput)
            print('Enter a number (1-5)')
    except ValueError:
        print('Value error:', userinput)
        print('Enter a number (1-5)')

if userinput == 1:
    listOptions()
elif userinput == 2:
    print('Enter search term:')
    userinput = input()
elif userinput == 3:
    print('Insert')
elif userinput == 4:
    print('Delete')
elif userinput == 5:
    print('Quit')
else:
    print('Enter a number (1-5)')
