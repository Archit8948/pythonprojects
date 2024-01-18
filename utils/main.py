from utils import database

menu_option = {
    'a': database.add_books,
    's': database.show_all_books,
    'd': database.delete_books,
    'r': database.edit_reading_status
}


def menu_to_show():
    database.create_book_table()
    show = input('add to add books , show to show all books , delete to delete books or q to quit: ')
    while show != 'q':
        if show.lower() in menu_option:
            selected = menu_option[show]
            selected()
        else:
            print('invalid input')
        show = input('add to add books , show to show all books , delete to delete books or q to quit: ')


menu_to_show()

