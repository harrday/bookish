from library_commands import Library
from library_constants import *
from datetime import datetime, timedelta


lc = LIBRARY_COMMANDS


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

    library = Library()
    library.addbookcomm(name, author, genre)

    print(f'{name} has been added!')

    returntomenu()


def viewbooks():  # TODO ADD GENRES ETC
    library = Library()
    library.viewbookcomm()
    returntomenu()

def editbooks():
    bookupdate = input('What book would you like to update?')
    library = Library()
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
    bookupdate = input('What book would you like to delete the details of?')
    library = Library()
    if library.checkbookexists(bookupdate):
        pass
    else:
        print('Book was not found')
        editbooks()
    valueupdate = input('Would attribute would you like to clear: \n'
                        '1: Book Title \n'
                        '2: Book Author \n'
                        '3: Book Genre')  # TODO reduce overlap with editbook()
    if valueupdate == '1':
        library.edittitlecomm(bookupdate, None)
    elif valueupdate == '2':
        library.editauthorcomm(bookupdate, None)
    elif valueupdate == '3':
        library.editgenrecomm(bookupdate, None)
    else:
        print('That is not a valid option... please try again')
        editbooks()
    returntomenu()


def addmembers():  # TODO make member functions a separate class?
    name = input('Please enter the first and last name of the new member:')
    try:
        fname, lname = name.split()
    except ValueError:
        print('Incorrect name format. Try: FIRSTNAME LASTNAME')
        addmembers()
    library = Library()
    library.addmembercomm(fname, lname)

    print(f'Member {fname} {lname} has been added!')

    print(f'What would you like to do now?:')
    returntomenu()

def checkout(): #TODO add in either member's/Book's name OR id
    member = input('Please enter the users name:')
    book = input('Please enter the book\'s title')
    #TODO check user/book in database - error safety
    library = Library()
    memberid = library.getidfrommember(member)
    bookid = library.getidfrombook(book)
    now = datetime.now()
    loandate = now.strftime("%d/%m/%Y")
    loanduration = LOAN_DURATION
    duedate = (now + timedelta(days=loanduration)).strftime("%d/%m/%Y")
    library.createloan(memberid, bookid, loandate, duedate)
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
    print('Goodbye!')
    return

def rerundb():
    library = Library()
    library.setUpLibrary()
    returntomenu()
