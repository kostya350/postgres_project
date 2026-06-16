from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS categories (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS books (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    year INTEGER,
    category_id INTEGER REFERENCES categories(id)
);
""")

cur.execute("INSERT INTO categories (name) VALUES ('Программирование') ON CONFLICT DO NOTHING;")
cur.execute("INSERT INTO categories (name) VALUES ('Художественная') ON CONFLICT DO NOTHING;")

cur.execute("""
INSERT INTO books (title, author, year, category_id)
VALUES ('Python для начинающих', 'Константин', 2026, 1)
ON CONFLICT DO NOTHING;
""")

cur.execute("""
INSERT INTO books (title, author, year, category_id)
VALUES ('Война и мир', 'Толстой', 1869, 2)
ON CONFLICT DO NOTHING;
""")

conn.commit()
cur.close()
conn.close()

print("База данных инициализирована!")
