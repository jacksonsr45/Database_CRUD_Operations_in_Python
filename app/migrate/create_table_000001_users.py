from app.migrate import migrate 

class create_table_000001_users(migrate.Migrate): 
	def __init__(self):
		super().__init__()

	def table_name(self):
		table_name = 'users'
		return table_name

	def table(self):
		table = [
			"id INT PRIMARY KEY NOT NULL AUTO_INCREMENT",
			"name VARCHAR(255) NOT NULL" ,
			"last_name VARCHAR(255) NOT NULL" ,
			"phone VARCHAR(255) NOT NULL unique" ,
			"created_at TIMESTAMP NULL",
			"updated_at TIMESTAMP NULL DEFAULT CURRENT_TIMESTAMP"
		]
		return table