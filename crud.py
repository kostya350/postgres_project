from sqlalchemy.orm import Session
from models import Category, Book

# ---------- Категории ----------
def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Category).offset(skip).limit(limit).all()

def get_category(db: Session, category_id: int):
    return db.query(Category).filter(Category.id == category_id).first()

def create_category(db: Session, title: str):
    db_category = Category(title=title)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def update_category(db: Session, category_id: int, title: str):
    db_category = get_category(db, category_id)
    if db_category:
        db_category.title = title
        db.commit()
        db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    db_category = get_category(db, category_id)
    if db_category:
        db.delete(db_category)
        db.commit()
    return db_category

# ---------- Книги ----------
def get_books(db: Session, skip: int = 0, limit: int = 100, category_id: int = None):
    query = db.query(Book)
    if category_id:
        query = query.filter(Book.category_id == category_id)
    return query.offset(skip).limit(limit).all()

def get_book(db: Session, book_id: int):
    return db.query(Book).filter(Book.id == book_id).first()

def create_book(db: Session, title: str, description: str, price: float, url: str, category_id: int):
    db_book = Book(
        title=title,
        description=description,
        price=price,
        url=url,
        category_id=category_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book

def update_book(db: Session, book_id: int, title: str = None, description: str = None, price: float = None, url: str = None):
    db_book = get_book(db, book_id)
    if db_book:
        if title is not None:
            db_book.title = title
        if description is not None:
            db_book.description = description
        if price is not None:
            db_book.price = price
        if url is not None:
            db_book.url = url
        db.commit()
        db.refresh(db_book)
    return db_book

def delete_book(db: Session, book_id: int):
    db_book = get_book(db, book_id)
    if db_book:
        db.delete(db_book)
        db.commit()
    return db_book