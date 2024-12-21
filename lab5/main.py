from xlitte_db.LibrarySystem import *
from xlitte_library_UI import ConsoleUI

library = Library()
library.db_context.Set("dbname=CSP_db host=localhost user=postgres password='Dsbuhsdf.gentdre1' port=5432")



ConsoleUI.Use(library)



# book_gen_rule = DataGeneratorConfig()
# author_gen_rule = DataGeneratorConfig()
# user_gen_rule = DataGeneratorConfig()

# titles = [f"Book - {x}" for x in range(10000)]
# book_gen_rule.add_generation_rule("title", titles)

# dates = [f"{day}.{mounth}.{year}" for day, mounth, year in zip([randint(1, 28) for i in range(10000)], [randint(1, 12) for i in range(10000)], [randint(1950, 2024) for i in range(10000)])]
# book_gen_rule.add_generation_rule("realese_date", dates)

# discs = [f"Description - {x}" for x in range(10000)]
# book_gen_rule.add_generation_rule("short_description", discs)

# author_names = [f"Name - {x}" for x in range(10000)]
# author_gen_rule.add_generation_rule("name", author_names)

# user_firstnames = ["Владислав", "Андрей", "Антон", "Семен", "Григорий", "Роман", "Дмитрий", "Арсений", "Сергей"]
# user_gen_rule.add_generation_rule("first_name", user_firstnames)

# telephones = ["+7" + "".join([str(randint(0, 9)) for i in range(9)]) for i in ran1ge(100)]
# user_gen_rule.add_generation_rule("telephone", telephones)

# # generated_books = book_gen_rule.generate_data(Library.Book, 1)
# #generated_authors = author_gen_rule.generate_data(Library.Author, 1000)

# books = [Library.Book(title, realese_date) for title, realese_date in zip(titles, dates)]
# authors = [Library.Author(firstname, "") for firstname in author_names]

# generated_users = user_gen_rule.generate_data(Library.User, 10)

# # book = Library.Book("Чернильные сны 2", "21.05.2024", "Сюрреалистическая книга задевающая тему пороков человека.")
# # books = [book]

# # print(generated_users)

# # library.add_user(generated_users)

# user_1 = library.get_entity_by_id(1, Library.User, "users")
# users = library.get_all_users()

# book_21 = library.get_entity_by_id(21, Library.Book, "books")

# library.rent_book_to_user(user_1, book_21)

# print(users, user_1)

