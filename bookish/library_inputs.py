from library_commands import Library
from library_constants import *
from datetime import datetime, timedelta

lc = LIBRARY_COMMANDS
library = Library()


# TODO add library = Library() as a global variable

def mainMenu():
    for i in list(lc):
        print(f'{i} : {lc[i][0]}')
    select = input('')

    try:
        eval(lc[int(select)][1])
    except ValueError:
        print("That's not a valid option, try again")
        mainMenu()


def addbooks():
    name = input('Please enter the name of the book:')
    author = input('Please enter the author of the book:')
    genre = input('Please enter the genre of the book:')

    library.addbookcomm(name, author, genre)

    print(f'{name} has been added!')

    returntomenu()
    return


def viewbooks():  # TODO ADD GENRES ETC
    rows = library.viewbookcomm()
    if len(rows) == 0:
        print('There are no books in the library!')
        yn = 0
        while yn != 'y' and yn != 'n':
            yn = input('Would you like to add some? (y/n)')
            if yn == 'y':
                addbooks()
                return
            elif yn == 'n':
                returntomenu()
                return
            else:
                print('That is not a valid option!')
    else:
        for row in rows:
            print(row)
    returntomenu()


def editbooks():
    bookupdate = input('What book would you like to update?')
    if library.checkbookexists(bookupdate):
        pass
    else:
        print('Book was not found')
        editbooks()
    valueupdate = input('Would you like to update: \n'
                        '1: Book Title \n'
                        '2: Book Author \n'
                        '3: Book Genre')
    textupdate = input('What is the new value?')  # TODO put these all in one def in library_commands
    if valueupdate == '1':
        library.edittitlecomm(bookupdate, textupdate)
    elif valueupdate == '2':
        library.editauthorcomm(bookupdate, textupdate)
    elif valueupdate == '3':
        library.editgenrecomm(bookupdate, textupdate)
    else:
        print('That is not a valid option... please try again')
        editbooks()
    returntomenu()


def deletedetails():
    book = input('What book would you like to delete?')
    if library.checkbookexists(book):
        pass
    else:
        print('Book was not found')
        deletedetails()
    library.deletebook(book)
    returntomenu()


def addmembers():
    name = input('Please enter the first and last name of the new member:')
    try:
        fname, lname = name.split()
    except ValueError:
        print('Incorrect name format. Try: FIRSTNAME LASTNAME')
        addmembers()
    library.addmembercomm(fname, lname)

    print(f'Member {fname} {lname} has been added!')

    print(f'What would you like to do now?:')
    returntomenu()

    # TODO add in either member's/Book's name OR id
    # TODO check there are books/members to choose from

def checkout():
    bookcheck, membercheck = False, False
    member = input('Please enter the users name:')
    while not bookcheck:
        book = input('Please enter the book\'s title')
        if library.checkbookexists(book):
            bookcheck = True
        else:
            print('Book was not found')
    while not membercheck:
        member = input('Please enter the Member')
        if library.checkmemberexists(member):
            membercheck = True
        else:
            print('Member was not found')
    memberid = library.getidfrommember(member)
    bookid = library.getidfrombook(book)
    now = datetime.now()
    loandate = now.strftime("%d/%m/%Y")
    loanduration = LOAN_DURATION
    duedate = (now + timedelta(days=loanduration)).strftime("%d/%m/%Y")
    library.createloan(memberid, bookid, loandate, duedate)
    returntomenu()


def whichbooks():
    member = input('Please give the name of the member you wish to search:')
    memberid = library.getidfrommember(member)
    bookstomember = library.getMembersBooks(memberid)
    print(bookstomember)
    returntomenu()


def returntomenu():
    ret = input('Would you like to return to the main menu (y/n):')
    if ret == 'y':
        mainMenu()
    elif ret == 'n':
        quitlib()
    else:
        print('invalid option')
        returntomenu()


def quitlib():
    library.closedb()
    print('Goodbye!')
    return


def rerundb():
    library = Library()
    library.setUpLibrary()
    returntomenu()
