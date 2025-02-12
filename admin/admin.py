import csv
import os
import sys
import pandas as pd
from database.database import Database

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '../database'))


class DatabaseChecker:
    def __init__(self, db: Database):
        self.db = db

    def load_cat_list(self) -> set:
        query = "SELECT name FROM cats"
        result = self.db.fetch_query(query)
        names = set()
        for row in result:

            names.add(row[0].strip())

        print(names)
        return names


class CSVEdit:
    def __init__(self, file: os.path):
        self.file = file

    def add_cat(self):
        try:
            cat_name = str(input("Enter cat's name: "))
            cat_age = int(input("Enter cat's age: "))
            if cat_age < 0:
                print("Age cannot be negative.")
                return
            cat_breed = str(input("Enter breed of cat: "))
            cat_color = str(input("Enter color of cat: "))
            cat_description = str(input("Enter description of cat: "))

            line = [cat_name, cat_age, cat_breed, cat_color, cat_description]
            with open(self.file, 'a', newline='') as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(line)

        except Exception as e:
            print(f"Error adding cat: {e}")

    def remove_cat(self):
        try:
            remove_name = str(input("Enter the name of the cat you want to remove: "))

            df = pd.read_csv(self.file)
            index_to_drop = df[df["Name"] == remove_name].index

            if not index_to_drop.empty:
                df = df.drop(index_to_drop)
                df.to_csv(self.file, index=False)
                print(f"Cat '{remove_name}' removed successfully.")
            else:
                print(f"Cat '{remove_name}' not found.")

        except Exception as e:
            print(f"Error adding cat: {e}")


class CatDataLoader:
    def __init__(self, db: Database, file_path: os.path):
        self.db = db
        self.file_path = file_path

    def load_and_replace_data(self):
        if not os.path.exists(self.file_path):
            print("Error: The specified file does not exist.")
            return

        try:
            with open(self.file_path, newline='', encoding='utf-8') as csvfile:
                reader = csv.DictReader(csvfile)
                header = reader.fieldnames

                if header is None or "Name" not in header:
                    print("Error: The provided CSV file is either empty or missing the 'name' column.")
                    return

                self.db.execute_query("DELETE FROM cats")

                for row in reader:
                    name = row["Name"].strip()
                    age = int(row["Age"])
                    breed = row["Breed"].strip()
                    color = row["Color"].strip()
                    description = row["Description"].strip()

                    self.db.execute_query("""
                        INSERT INTO cats (name, age, breed, color, description) VALUES (?, ?, ?, ?, ?)
                        
                    """, (name, age, breed, color, description))
        except Exception as e:
            print(f"Error processing file: {e}")

    def initialize_cat_table(self):
        self.db.execute_query("""
            CREATE TABLE IF NOT EXISTS cats (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT UNIQUE NOT NULL,
                age INTEGER,
                breed TEXT NOT NULL,
                color TEXT NOT NULL,
                description TEXT NOT NULL
            );
        """)
class Admin:
    def __init__(self, data_loader: CatDataLoader, checker: DatabaseChecker, edit: CSVEdit):
        self.data_loader = data_loader
        self.checker = checker
        self.edit = edit
    def runAdminTool(self):
        try:
            while True:
                print("\n~~~ Admin ~~~")
                print("Enter the numbers for the commands:")
                print("1. Check currently available cats")
                print("2. Add new cat to the database")
                print("3. Remove cat from the database")
                print("4. Quit")
                command = input("$ ").strip()

                if command == "4 ":
                    print("Exiting Administrator Tool.")
                    break
                elif command == "1":
                    self.checker.load_cat_list()
                elif command == "2":
                    self.edit.add_cat()
                    self.data_loader.initialize_cat_table()
                    self.data_loader.load_and_replace_data()
                elif command == "3":
                    self.edit.remove_cat()
                    self.data_loader.initialize_cat_table()
                    self.data_loader.load_and_replace_data()
                else:
                    print("Invalid command. Please choose one of the listed commands.")
        except KeyboardInterrupt:
            print("\nProcess interrupted.")


if __name__ == "__main__":
    DIR = os.path.dirname(os.path.abspath(__file__))

    db_path = os.path.join(DIR, "../database/cats.db")
    csv_path = os.path.join(DIR, "../cats.csv")
    db = Database(db_path)

    data_loader = CatDataLoader(db, csv_path)
    checker = DatabaseChecker(db)
    edit = CSVEdit(csv_path)
    admin_tool = Admin(data_loader, checker, edit)

    admin_tool.runAdminTool()
    db.close()
