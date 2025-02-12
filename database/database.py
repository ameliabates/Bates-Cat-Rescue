import sqlite3
from typing import List, Tuple


class Database:
    def __init__(self, db_file: str):
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

    def execute_query(self, query: str, params: Tuple = ()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetch_query(self, query: str, params: Tuple = ()) -> List[Tuple]:
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def initialize_schema(self, schema_file: str):
        with open(schema_file, 'r') as file:
            schema = file.read()
            self.cursor.executescript(schema)
        self.connection.commit()

    def close(self):
        self.connection.close()


class Cat:
    def __init__(self, db: Database):
        self.db = db

    def insert_cat(self, name: str, age: int, breed: str, color: str, description: str ):
        query = "INSERT INTO cats (name, age, breed, color, description) VALUES (?, ?, ?, ?, ?)"
        self.db.execute_query(query, (name, age, breed, color, description))

