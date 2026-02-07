import sqlite3
import rsa
import hashlib
class Databaser:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def create_database(self, name):
        with open(name, 'a') as file:
            file.write('')
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Passwords(id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(100), password_rsa VARCHAR(1000))''')
        self.connection.commit()
    def request(self, request, data = None):
        self.cursor.execute(request, data)
        return self.cursor.fetchall()
    def modificate(self, modification, data = None):
        self.cursor.execute(modification, data)
        self.connection.commit()