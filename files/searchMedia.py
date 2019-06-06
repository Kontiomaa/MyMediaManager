from files.db import runSearch

def searchOptions():

    dboptions = [['("m_name") AS media_name', 'media', 'media_name'], ['(ms_name) AS set_name', 'mediaset', 'set_name'], ['(c_name) AS category_name', 'category', 'category_name'], ['(t_name) AS tag_name', 'tag', 'tag_name'], ['(a_firstname || " " || a_lastname) AS a_name', 'artist', 'a_name']]

    print('Search for:')
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
                print('Enter search term:')
                userTerm = str(input())
                runSearch(dboptions[userinput-1], userTerm)
                break
            else:
                print('Enter a number (1-5)')
        except ValueError:
            print('Enter a number (1-5)')
