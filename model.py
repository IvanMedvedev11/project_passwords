import sqlite3
import rsa
class Databaser:
    def __init__(self):
        self.connection = None
        self.cursor = None
    def create_database(self, name):
        with open(name, 'a') as file:
            file.write('')
        self.connection = sqlite3.connect(name)
        self.cursor = self.connection.cursor()
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Passwords(id INTEGER PRIMARY KEY AUTOINCREMENT, login VARCHAR(100), password_rsa VARCHAR(1000), target VARCHAR(1000))''')
        self.connection.commit()
    def request(self, request, data = ()):
        self.cursor.execute(request, data)
        return self.cursor.fetchall()
    def modificate(self, modification, data = ()):
        self.cursor.execute(modification, data)
        self.connection.commit()
class Encrypter:
    def __init__(self, private_key = None):
        with open('public_key.pem', 'a+b') as file1:
            file1.seek(0)
            with open("private_key.pem", 'a+b') as file2:
                file2.seek(0)
                try:
                    self.public_key = rsa.PublicKey.load_pkcs1(file1.read())
                except ValueError:
                    self.public_key, self.private_key = rsa.newkeys(512)
                    file1.write(self.public_key.save_pkcs1())
                    file2.write(self.private_key.save_pkcs1())
                    print(f"Ваш приватный ключ: {self.private_key}")
                else:    
                    self.private_key = rsa.PrivateKey.load_pkcs1(file2.read())
                    if str(self.private_key) != private_key:
                        raise Exception("Неверный ключ")
    def encrypt(self, password):
        encrypted = rsa.encrypt(password.encode(), self.public_key).hex()
        return encrypted
    def decrypt(self, password):
    	password = bytes.fromhex(password)
    	decrypted = rsa.decrypt(password, self.private_key).decode()
    	return decrypted
                    
                
        
