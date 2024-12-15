import psycopg2 as psql
from dataclasses import dataclass, fields
from random import randint

class Db_context:
        
    def __init__(self):
        self.connection_string = ""
        self.conn = None
        self.cursor = None

    def Set(self, connection_string: str):
        try:
            self.connection_string = connection_string
            self.conn = psql.connect(connection_string)
            self.cursor = self.conn.cursor()
            print("Successfully connected to database.")
        except:
            raise Exception("Was unable to connect to database. Please, specify connection string. You can do it by Db_context.Set(connection_string) on Library object.")

class Library:
    
    @dataclass
    class Book:
        title: str
        realese_date: str
        short_description: str

    @dataclass
    class Author:
        name: str

    def __init__(self):
        self.db_context = Db_context()

    def __del__(self):
        if(self.db_context.conn != None):
            self.db_context.cursor.close()
            self.db_context.conn.close()
            print("Connection was successfully closed.")


    def add_books(self, books: list[Book] | Book):
        sql_query = ""
        column_names = [field.name for field in fields(Library.Book)]
        columns_placeholder = ', '.join(column_names)
        values_placeholder = ', '.join(['%s'] * len(column_names))

        if isinstance(books, list):
            for book in books:
                sql_query = f"INSERT INTO \"books\" ({columns_placeholder}) VALUES ({values_placeholder});\n"
                book_data = tuple(getattr(book, name) for name in column_names)
                
                self.db_context.cursor.execute(sql_query, book_data)
            
            self.db_context.conn.commit()

    def add_author(self, authors: list[Author] | Author):
        sql_query = ""
        column_names = [field.name for field in fields(Library.Author)]
        columns_placeholder = ', '.join(column_names)
        values_placeholder = ', '.join(['%s'] * len(column_names))

        if isinstance(authors, list):
            for author in authors:
                sql_query = f"INSERT INTO \"authors\" ({columns_placeholder}) VALUES ({values_placeholder});\n"
                author_data = tuple(getattr(author, name) for name in column_names)
                
                self.db_context.cursor.execute(sql_query, author_data)
            
            self.db_context.conn.commit()

class DataGeneratorConfig:

    generation_data: dict[str, list]

    def __init__(self):
        self.generation_data = {}
    
    def add_generation_rule(self, column_name:str, generation_rule: list):
        self.generation_data[column_name] = generation_rule

    def generate_data(self, dataType: type, n: int) -> list[type]:

        generated_data: list = []
        for i in range(n):
            obj = {}
            for field in fields(dataType):
                rule = self.generation_data.get(field.name, None)
                if(rule != None):
                    obj[field.name] = self.pick_random_data(rule)
    
            generated_item = dataType(**obj)
            generated_data.append(generated_item)

        return generated_data

    def pick_random_data(self, data: list):
        return data[randint(0, len(data)-1)]




