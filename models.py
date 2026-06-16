class Category:
    def __init__(self, id, name):
        self.id = id
        self.name = name

class Book:
    def __init__(self, id, title, author, year, category_id):
        self.id = id
        self.title = title
        self.author = author
        self.year = year
        self.category_id = category_id
