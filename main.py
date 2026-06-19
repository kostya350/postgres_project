from db import SessionLocal, engine
from models import Base
from crud import get_categories, get_books

# Создаём таблицы через SQLAlchemy (вместо ручных SQL-запросов)
Base.metadata.create_all(bind=engine)

def main():
    db = SessionLocal()

    print("Категории:")
    for row in get_categories(db):
        print(f"  {row.id}: {row.title}")

    print("\nКниги:")
    for row in get_books(db):
        print(f"  {row.id}: {row.title} - {row.price} руб.")

    db.close()

if __name__ == "__main__":
    main()