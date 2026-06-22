from src.db import SessionLocal, engine
from src.models import Base, Category, Book

def init_db():
    # 1. Создаём таблицы в правильном порядке (это исправляет твою ошибку)
    Base.metadata.create_all(bind=engine)
    print("Таблицы созданы (или уже существуют).")

    db = SessionLocal()

    # Очищаем старые данные
    db.query(Book).delete()
    db.query(Category).delete()
    db.commit()

    # Создаём категории
    cat1 = Category(title="Программирование")
    cat2 = Category(title="Художественная литература")
    db.add_all([cat1, cat2])
    db.commit()

    # Книги для категории "Программирование" (4 книги)
    books = [
        Book(
            title="Чистый код",
            description="Книга о принципах написания чистого кода",
            price=25.99,
            url="https://example.com/clean-code",
            category_id=cat1.id
        ),
        Book(
            title="Изучаем Python",
            description="Книга для начинающих программистов на Python",
            price=18.50,
            url="https://example.com/learning-python",
            category_id=cat1.id
        ),
        Book(
            title="Алгоритмы и структуры данных",
            description="Базовые алгоритмы для разработчиков",
            price=30.00,
            url="https://example.com/algorithms",
            category_id=cat1.id
        ),
        Book(
            title="Flask: создание веб-приложений",
            description="Руководство по Flask для создания веб-приложений",
            price=22.00,
            url="https://example.com/flask",
            category_id=cat1.id
        ),
        # Книги для категории "Художественная литература" (2 книги)
        Book(
            title="Война и мир",
            description="Эпический роман Льва Толстого",
            price=12.00,
            url="https://example.com/war-and-peace",
            category_id=cat2.id
        ),
        Book(
            title="Преступление и наказание",
            description="Роман Фёдора Достоевского о морали и преступлении",
            price=10.00,
            url="https://example.com/crime-and-punishment",
            category_id=cat2.id
        ),
    ]

    db.add_all(books)
    db.commit()
    db.close()
    print("База данных инициализирована!")

if __name__ == "__main__":
    init_db()