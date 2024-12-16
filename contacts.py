import sqlite3
import os

class Contacts:
	def __init__(self):
		self.class_variable = " "
	def set_database_name(self,database_file):
		self.class_variable = database_file
		if os.path.exists(database_file):
			return
		else:
			work = sqlite3.connect(database_file)
			worker = work.cursor()

			worker.execute('''CREATE TABLE IF NOT EXISTS contacts (
			contact_id INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
			first_name TEXT NOT NULL,
			last_name TEXT NOT NULL)''')

			worker.execute('''CREATE TABLE IF NOT EXISTS phones (
			phone_id INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
			contact_id INTEGER NOT NULL REFERENCES contacts(contact_id),
			phone_type TEXT NOT NULL,
			phone_number TEXT NOT NULL)''')

			work.commit()
			work.close()

	def get_database_name():
		return class_variable

	def add_contact(self,first_name, last_name):
		work = sqlite3.connect(self.class_variable)
		worker = work.cursor()
		worker.execute('''INSERT INTO contacts (first_name, last_name) VALUES (?,?)''', (first_name, last_name))

		work.commit()
		work.close()

	def modify_contact(self,contact_id, first_name, last_name):
		work = sqlite3.connect(self.class_variable)
		worker = work.cursor()

		upd = 'UPDATE contacts SET first_name = ?, last_name = ? WHERE contact_id = ?'
		worker.execute(upd,(first_name,last_name ,contact_id))

		work.commit()
		work.close()

	def add_phone(self,contact_id, phone_type, phone_number):
		work = sqlite3.connect(self.class_variable)
		worker = work.cursor()

		worker.execute('''INSERT INTO phones (contact_id, phone_type, phone_number) VALUES (?,?,?)''',(contact_id, phone_type, phone_number))

		work.commit()
		work.close()

	def modify_phone(self,phone_id, phone_type, phone_number):
		work = sqlite3.connect(self.class_variable)
		worker = work.cursor()
		upd = 'UPDATE phones SET phone_number=?, phone_type=? WHERE phone_id = ?'
		worker.execute(upd,(phone_number,phone_type,phone_id))

		work.commit()
		work.close()

	def get_contact_phone_list(self):
		work = sqlite3.connect(self.class_variable)
		worker = work.cursor()

		worker.execute('''SELECT contacts.*, phones.* FROM contacts LEFT JOIN phones ON contacts.contact_id=phones.contact_id''')
		temp = worker.fetchall()


		work.commit()
		work.close()
		return temp
