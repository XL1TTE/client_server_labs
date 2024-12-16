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
        is_rented: bool
        id: int | None = None

    @dataclass
    class Author:
        first_name: str
        last_name: str
        id: int | None = None

    @dataclass
    class User:
        first_name: str
        telephone: str
        id: int | None = None


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

    def add_user(self, users: list[User] | User):
        sql_query = ""
        column_names = [field.name for field in fields(Library.User)]
        columns_placeholder = ', '.join(column_names)
        values_placeholder = ', '.join(['%s'] * len(column_names))

        if isinstance(users, list):
            for user in users:
                sql_query = f"INSERT INTO \"users\" ({columns_placeholder}) VALUES ({values_placeholder});\n"
                user_data = tuple(getattr(user, name) for name in column_names)
                
                self.db_context.cursor.execute(sql_query, user_data)
            
            self.db_context.conn.commit()

    def get_all_users(self):
        column_names = set(field.name for field in fields(Library.User))
        columns_placeholder = ', '.join(column_names)

        users: list[Library.User] = []
        self.db_context.cursor.execute(f"SELECT {columns_placeholder} FROM users")
        rows = self.db_context.cursor.fetchall()

        for row in rows:
            user_data = {}
            for col_name, value in zip(column_names, row):
                user_data[col_name] = value
            
            users.append(Library.User(**user_data))
        
        return users

    def get_entity_by_id(self, id: int, entityType: type, table_name: str):

        column_names = [field.name for field in fields(entityType)]
        columns_placeholder = ', '.join(column_names)

        self.db_context.cursor.execute(f"SELECT {columns_placeholder} FROM {table_name} where id = {id};")
        rows = self.db_context.cursor.fetchall()

        for row in rows:
            entity_data = {}
            for field_name, value in zip(column_names, row):
                    entity_data[field_name] = value
            
            return entityType(**entity_data)

    def get_n_entities(self, entityType: type, table_name: str, n: int | None = None, start: int | None = None, order_by: str = "id"):
        column_names = [field.name for field in fields(entityType)]
        columns_placeholder = ', '.join(column_names)

        entities = []
        
        if(start == None and n == None):
            self.db_context.cursor.execute(f"SELECT {columns_placeholder} FROM {table_name};")
            rows = self.db_context.cursor.fetchall()
        else:
            self.db_context.cursor.execute(f"SELECT {columns_placeholder} FROM {table_name} ORDER BY {order_by} ASC LIMIT {n} OFFSET {start};")
            rows = self.db_context.cursor.fetchall()

        for row in rows:
            entity_data = {}
            for field_name, value in zip(column_names, row):
                    entity_data[field_name] = value
            
            entities.append(entityType(**entity_data))
        return entities
    
    def get_columns_info(self, table_name: str) -> dict[str, int]:
        self.db_context.cursor.execute(f"SELECT column_name, ordinal_position FROM information_schema.columns WHERE table_name = '{table_name}';")
        info = {}
        for data in self.db_context.cursor.fetchall():
            info[data[0]] = data[1] - 1

        return info

    def rent_book_to_user(self, user_id: int, book_id: int):
        try:
            self.db_context.cursor.execute(f"INSERT INTO \"user_takenbook\" (user_id, book_id) VALUES ({user_id}, {book_id});")
            self.db_context.cursor.execute(f"UPDATE \"books\" SET is_rented = true WHERE id = {book_id};")
            self.db_context.conn.commit()
        except:
            pass
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




