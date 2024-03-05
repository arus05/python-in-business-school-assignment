class Printer:

	def print_greeting():
		pass
	

	def print_menu():
		pass


class SalaryBook:

	def __init__(self, file_path):
		self.file_path = file_path
	

	def add_new_entry(self, name, years, department, salary):
		pass
	

	def display_all_entries(self):
		pass


	def delete_all_entries(self):
		pass
	

	def open_file(self):
		self.file = open(self.file_path)

	
	def close_file(self):
		self.file.close()