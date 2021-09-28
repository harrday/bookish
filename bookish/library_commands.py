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
                    MemberId,
                    Loan_Date,
                    Due_Date
                )'''

        members = '''
            CREATE TABLE IF NOT EXISTS members (
                MemberId INTEGER PRIMARY KEY AUTOINCREMENT, 
                FirstName,
                LastName
            )'''

        self.cursor.execute(book)
        self.cursor.execute(loans)
        self.cursor.execute(members)
        self.lib.commit()

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
        return

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

    def addmembercomm(self, fname, lname):
        params = (fname, lname)
        members = """
                    INSERT INTO members
                    (FirstName, LastName)
                    VALUES (?, ?)
                """
        self.cursor.execute(members, params)
        self.lib.commit()
        return

    def getidfrombook(self, book):
        books = """
                    SELECT *
                    FROM books
                    WHERE BookName = ?
        """
        self.cursor.execute(books, book)
        rows = self.cursor.fetchone()
        return rows[0]

    def getidfrommember(self, member):
        fname, lname = member.split()
        name = (fname, lname)
        members = """
                            SELECT *
                            FROM members
                            WHERE FirstName = ? AND LastName = ?
                """
        self.cursor.execute(members, name)
        rows = self.cursor.fetchone()
        return rows[0]

    def createloan(self, memberid, bookid, loandate, duedate):
        params = (bookid, memberid, loandate, duedate)
        loan = """
                    INSERT INTO loans
                    (BookId, MemberId, Loan_Date, Due_Date)
                    VALUES (?, ?, ?, ?)
                """
        self.cursor.execute(loan, params)
        self.lib.commit()
        return

    #TODO REMEMBER TO CLOSE DATABASE/LIBRARY


