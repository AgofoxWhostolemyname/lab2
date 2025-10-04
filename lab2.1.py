import csv

with open('books-en.csv', 'r', encoding='windows-1251') as file:
    reader = csv.DictReader(file, delimiter=';')
    books = list(reader)

long_titles = [book for book in books if len(book['Book-Title']) > 30]
print(f"1. Книг с названием длиннее 30 символов: {len(long_titles)}")

def search_by_author_price(author_name, min_price=200):
    results = []
    for book in books:
        try:
            price_str = book['Price'].replace(',', '.')
            price = float(price_str)
            
            if (author_name.lower() in book['Book-Author'].lower() and 
                price > min_price):
                results.append(book)
        except (ValueError, KeyError):
            continue
    return results

author = input("\n2. Введите имя автора для поиска (цена > 200 руб.): ")
author_results = search_by_author_price(author)
print(f"Найдено книг дороже 200 руб.: {len(author_results)}")
for i, book in enumerate(author_results, 1):
    price = book['Price'].replace(',', '.')
    print(f"{i}. {book['Book-Title']} - {book['Book-Author']} - {price} руб.")

import random

selected_books = random.sample(books, min(20, len(books)))
with open('bibl.txt', 'w', encoding='utf-8') as f:
    for i, book in enumerate(selected_books, 1):
        ref = f"{book['Book-Author']}. {book['Book-Title']}-{book['Year-Of-Publication']}"
        f.write(f"{i}. {ref}\n")

print(f"\n3. Создан файл 'bibl.txt")