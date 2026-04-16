class Viewer:
	def show_table(self, columns, data):
		print('===========================')
		print('===========================')
		for column in columns:
			print(column, end='                    ')
		for row in data:
			print()
			for elem in row:
				print(elem, end='                  ')
		print()
		print('===========================')
		print('===========================')
