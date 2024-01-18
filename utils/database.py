import sqlite3


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key,author text,read integer)')
    connection.commit()
    connection.close()


def add_books():
    name = input('please enter the name of book: ')
    author = input('please enter the name of author: ')
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO books VALUES(?, ?, 0)', (name, author))
    connection.commit()
    connection.close()


def search_books():  # this is incomplete
    name = input("please enter name of book you want to search: ")
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT name, author FROM books WHERE name = ?', (name,))
    connection.close()


def get_files():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM books')
    cursor.fetchall()
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in cursor.fetchall()]
    connection.close()
    return books


def show_all_books():
    print('hello')
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    single = cursor.fetchall()
    books = [{'name': row[0], 'author': row[1], 'read': row[2]} for row in single]
    for book in books:
        print(f'name of book: {book["name"]}, author: {book["author"]}, read status: {book["read"]}')
    connection.close()


def delete_books():
    delete = input('enter book to delete: ')
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM books WHERE name = ?', (delete,))
    connection.commit()
    connection.close()


def edit_reading_status():
    update = input('enter book you have read: ')
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE books SET read = 1 WHERE name = ?', (update,))
    connection.commit()
    connection.close()
