import sqlite3

#Словарь названий колонок в базе данных(id в данном списке нет)
column_list = ['lastname', 'firstname', 'second', 'phone']

class PhoneBook():
	'''Класс направленный на работу с базой данных(SQLite). Принимает в качестве аргументов:
	id, lastname, firstname, secondname, phone. А в качестве параметров по умолчанию установлены
	'NULL'. В классе имеется конструктор __init__, метод add_number(self) для добавления пользователей,
	метод del_phone(self) для удаления пользователей, и метод find_phone(other)для поиска пользователей
	по БД. 
	'''
	def __init__(self, id='NULL', lastname='NULL', firstname='NULL', secondname='NULL', phone='NULL'):
		self.conn = sqlite3.connect('Phonebook.db') #Имя базы данных не забудьте изменить
		self.curs = self.conn.cursor()
		self.id = id
		self.lastname = lastname
		self.firstname = firstname
		self.secondname = secondname
		self.phone = phone
	def add_number(self):
		'''Добавляет в БД новые записи. Если не был передан один из аргументов, то 
		в базу данных запись будет внесена с пустыми полями.
		'''
		ins = 'INSERT INTO PhoneBook(lastname, firstname, second, phone) VALUES(?, ?, ?, ?)'
		self.curs.execute(ins, (self.lastname, self.firstname, self.secondname, self.phone))
		self.conn.commit()
		self.curs.close()
		self.conn.close()
	def del_phone(self):
		'''Удаление записей по id. Для удаления требуется создать экземпляр с 
		переданным id.'''
		try:
			phone_del = self.conn.execute('DELETE FROM PhoneBook WHERE id=?' , (self.id, ))
			self.conn.commit()
		except sqlite3.OperationalError:
			print("Database Error")
		finally:
			self.curs.close()
			self.conn.close()

	def find_phone(other):
		'''Функция поиска пользователей в базе данных. Принимает как целое слово так и часть
		слова. Если запустить функцию без параметров - выведет информацию по всем пользователям.

		'''
		conn = sqlite3.connect('Phonebook.db')
		curs = conn.cursor()
		find_list = []
		for a in column_list:
			fin = ("SELECT * FROM PhoneBook ""WHERE %s LIKE ?") % a
			for title in curs.execute(fin,(['%'+other+'%'])):
				find_list.append(title)
				#Удобочитаемый вывод найденной информации:
				#print('ID:', title[0], '|Фамилия:', title[1],'|Имя:', title[2],'|Отчество:', title[3],'|Телефон:', title[4])
			return find_list
		return curs.close(), conn.close()

