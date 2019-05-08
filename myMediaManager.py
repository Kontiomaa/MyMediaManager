from initdb import initdb

initdb()

print('What do you want to do?')
print('1. List')
print('2. Search')
print('3. Insert')
print('4. Delete')

while True:
    try:
        userinput = int(input())
        break
    except ValueError:
        print('Enter a number (1-4)')

#if userinput()
