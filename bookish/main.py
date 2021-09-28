from library_commands import Library
from library_inputs import *

def main():
    print('Welcome to the library, here you can:')
    # Setting up all the databases (books, copies, loans, members)
    Library().setUpLibrary()
    mainMenu()


if __name__ == '__main__':
    main()
