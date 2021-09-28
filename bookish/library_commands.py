import sqlite3
from sqlite3 import Error

class Library:

    def __init__(self):
        try:
            lib = sqlite3.connect('databases/library.db')
        except Error as e:
            print(e)
            return
        cursor = lib.cursor()
        self.lib = lib
        self.cursor = cursor



    def setUpLibrary(self):

        book = '''
            CREATE TABLE IF NOT EXISTS books (
                BookId INTEGER PRIMARY KEY AUTOINCREMENT, 
                BookName,
                BookAuthor,
                BookGenre
            )'''

        loans = '''
                CREATE TABLE IF NOT EXISTS loans (
                    BookId,
                    CustomerId,
                    Loan_Date,
                    Due_Date
                )'''

        members = '''
            CREATE TABLE IF NOT EXISTS members (
                CustomerId INTEGER PRIMARY KEY AUTOINCREMENT, 
                FirstName,
                LastName
            )'''

        self.cursor.execute(book)
        self.cursor.execute(loans)
        self.cursor.execute(members)

    def addbookcomm(self, name, author, genre):
        params = (name, author, genre)
        book = """
            INSERT INTO books
            (BookName, BookAuthor, BookGenre)
            VALUES (?, ?, ?)
        """
        self.cursor.execute(book, params)
        self.lib.commit()
        return

    def viewbookcomm(self):
        view_books = 'SELECT * FROM books'
        self.cursor.execute(view_books)

        rows = self.cursor.fetchall()
        for row in rows:
            print(row)

    def checkbookexists(self, bookupdate):
        check = """
            SELECT *
            FROM books
            WHERE BookName = ?
            """

        self.cursor.execute(check, bookupdate)
        rows = self.cursor.fetchall()
        if len(rows) != 0:
            return True
        else:
            return False

    def edittitlecomm(self, bookupdate, textupdate):

        update = """
            UPDATE books
            SET BookName = ?
            WHERE BookName = ?
            """

        self.cursor.execute(update, (textupdate, bookupdate))
        self.lib.commit()
        return

    def editauthorcomm(self, bookupdate, textupdate):

        update = """
            UPDATE books
            SET BookAuthor = ?
            WHERE BookName = ?
            """

        self.cursor.execute(update, (textupdate, bookupdate))
        self.lib.commit()
        return

    def editgenrecomm(self, bookupdate, textupdate):

        update = """
            UPDATE books
            SET BookGenre = ?
            WHERE BookName = ?
            """

        self.cursor.execute(update, (textupdate, bookupdate))
        self.lib.commit()
        return

    #TODO REMEMBER TO CLOSE DATABASE/LIBRARY


