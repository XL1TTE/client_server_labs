from xlitte_db.LibrarySystem import *
from argparse import *
import os
import time

CurrentPage = 1
PageContentLimit = 10

def Use(library_system: Library):

    while(True):
        clear_console()
        __welcome__()
        __show__book_list__(library_system)

        __show_commands__()
        command = int(input("Введите номер команды: "))

        match(command):
            case 1:
                __show_next_book_page__(library_system)
            
            case 2:
                __show_previous_book_page__(library_system)
                
            case 3:
                __rent_book__(library_system)
                time.sleep(5)
            case 4:
                break


def __welcome__():
    message = f"Добро пожаловать в систему xlitte library. \n\n"

def __show_next_book_page__(library_system: Library):
    global CurrentPage
    global PageContentLimit

    CurrentPage += 1


def __show_previous_book_page__(library_system: Library):
    global CurrentPage
    global PageContentLimit

    if(CurrentPage > 1):
        CurrentPage -= 1

def __show__book_list__(library_system: Library):
    global CurrentPage
    global PageContentLimit

    start = (CurrentPage - 1) * PageContentLimit

    message = f"Список доступных книг: \n"

    isTakenRu_Translate = {
        True: "Да",
        False: "Нет"
    }

    books = library_system.get_n_entities(Library.Book, 'books', start=start, n=PageContentLimit, order_by="id")

    for book in books:
        message += f"{book.id}. Книга - {book.title}, выпущенная - {book.realese_date}, доступна для аренды: {isTakenRu_Translate[not book.is_rented]}. \n"

    print(message)

def __rent_book__(library_system: Library):
    user_id = int(input("Ваш идентификационный номер?: "))
    book_id = int(input("Книгу под каким номером желаете взять?: "))


    try:
        clear_console()
        book = library_system.get_entity_by_id(book_id, Library.Book, 'books')
        if(not book.is_rented):
            library_system.rent_book_to_user(user_id, book_id)
            user = library_system.get_entity_by_id(user_id, Library.User, 'users')
            print(f"Книга под номером {book_id} успешно арендована! \nПриятного чтения {user.first_name}.")
        else:
            print("Данная книга уже арендована другим пользователем.")
    except:
        print("Что-то пошло не так, возможно ввели не сущесвующий номер книги или пользователя.")

def __show_commands__():
    message = "\nСписок команд: \n"

    message += "1. Следующая страница. \n"
    message += "2. Предыдущая страница. \n"
    message += "3. Арендовать книгу. \n"
    message += "4. Выход. \n"

    print(message)


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')
