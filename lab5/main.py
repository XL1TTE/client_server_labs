from xlitte_db.LibrarySystem import *

library = Library()
library.db_context.Set("dbname=CSP_db host=localhost user=postgres password='Dsbuhsdf.gentdre1' port=5432")

book_gen_rule = DataGeneratorConfig()
author_gen_rule = DataGeneratorConfig()

titles = [f"Book - {x}" for x in range(10)]
book_gen_rule.add_generation_rule("title", titles)

dates = [f"{day}.{mounth}.{year}" for day, mounth, year in zip([randint(1, 28) for i in range(10000)], [randint(1, 12) for i in range(10000)], [randint(1950, 2024) for i in range(10000)])]
book_gen_rule.add_generation_rule("realese_date", dates)

discs = [f"Description - {x}" for x in range(10)]
book_gen_rule.add_generation_rule("short_description", discs)

author_names = [f"Name - {x}" for x in range(10)]
author_gen_rule.add_generation_rule("name", author_names)

generated_books = book_gen_rule.generate_data(Library.Book, 1)
#generated_authors = author_gen_rule.generate_data(Library.Author, 1000)

# book = Library.Book("Чернильные сны 2", "21.05.2024", "Сюрреалистическая книга задевающая тему пороков человека.")
# books = [book]

library.add_books(generated_books)
#library.add_author(generated_authors)

