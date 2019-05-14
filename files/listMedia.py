from files.db import requestList

def listOptions():

    dboptions = [['m_name', 'media'], ['ms_name', 'mediaset'], ['c_name', 'category'], ['t_name', 'tag'], ['(a_firstname || " " || a_lastname) AS a_name', 'artist']]

    print('List:')
    print('1. Media')
    print('2. Sets')
    print('3. Catergories')
    print('4. Tags')
    print('5. Artists')

    while True:
        try:
            userinput = None
            userinput = int(input())
            if 0 < userinput < 6:
                requestList(dboptions[userinput-1])
                break
            else:
                print('Enter a number (1-5)')
        except ValueError:
            print('Enter a number (1-5)')
