from crud import get_categories, get_books

print("Категории:")
for row in get_categories():
    print(f"  {row[0]}: {row[1]}")

print("\nКниги:")
for row in get_books():
    print(f"  {row[0]}: {row[1]} - {row[2]} ({row[3]})")
