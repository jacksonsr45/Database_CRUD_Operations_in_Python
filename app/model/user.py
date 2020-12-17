from app import model

class User(model.Model):
    def __init__(self):
        super().__init__()

    def table_name(self):
        return "users"