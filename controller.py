from model import *
from view import *
class Controller:
    def input_key(self):
    	private_key = input("Введите приватный ключ(или оставьте поле пустым, если ключ не создан: ")
    	if not private_key:
    		self.encoder = Encrypter()
    	else:
    		self.encoder = Encrypter(private_key)
    		print("Верный ключ")
    def actions(self):
    	while True:
    		action = input("Выберите действие: 1 - добавить новый пароль, 2 - изменить пароль, 3 - удалить пароль, 4 - вывести пароли, 5 - выполнить запрос к базе данных (для продвинутых), 6 - модифицировать базу данных (для продвинутых), 7 - завершить работу: ")
    		self.databaser = Databaser()
    		self.viewer = Viewer()
    		self.databaser.create_database('passwords.db')
    		if action == "1":
    			login = input('Введите логин: ')
    			password = input('Введите пароль: ')
    			target = input('Введите, для какого ресурса нужен пароль: ')
    			encrypted = str(self.encoder.encrypt(password))
    			self.databaser.modificate('INSERT INTO Passwords(login, password_rsa, target) VALUES (?, ?, ?)', (login, encrypted, target))
    			print('Пароль добавлен')
    		elif action == "2":
    			login = input('Введите логин: ')
    			target = input('Введите, для какого ресурса нужен пароль: ')
    			password = input('Введите новый пароль: ')
    			encrypted = self.encoder.encrypt(password)
    			self.databaser.modificate('UPDATE Passwords SET password_rsa = ? WHERE login = ? AND target = ?', (encrypted, login, target))
    			print('Пароль изменен')
    		elif action == '3':
    			login = input('Введите логин: ')
    			target = input('Введите, для какого ресурса нужен пароль: ')
    			self.databaser.modificate('DELETE FROM Passwords WHERE login = ? AND target = ?', (login, target))
    		elif action == '4':
    			data = list(self.databaser.request('SELECT login, password_rsa, target FROM Passwords'))
    			for i in range(len(data)):
    				data[i] = list(data[i])
    				data[i][1] = self.encoder.decrypt(data[i][1])
    			self.viewer.show_table(['Логин', 'Пароль', 'Ресурс'], data)
    		elif action == '5':
    			request = input('Введите запрос: ')
    			print('Результат работы:')
    			try:
    				print(self.databaser.request(request))
    			except Exception:
    				print('Некорректный запрос')
    		elif action == '6':
    			modification = input('Введите модификацию: ')
    			try:
    				self.databaser.modificate(modification)
    			except Exception:
    				print('Некорректный запрос')
    			else:
    				print('База данных изменена')
    		elif action == '7':
    			print('Завершение работы')
    			break
    		else:
    			print('Некорректный номер действия')
    			
