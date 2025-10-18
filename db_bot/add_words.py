import sqlite3
import json
import csv


def add_word_simple(english, russian):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    # Добавляем слово
    cursor.execute('INSERT INTO words (english, russian) VALUES (?, ?)',
                   (english, russian))
    conn.commit()
    conn.close()
    #print(f"Слово добавлено: {english} - {russian}")



with open('muellerdict_words.csv', 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    next(csv_reader)
    time=10
    for row in csv_reader:


       add_word_simple(row['source'], row['translations'])

    #for word in words:
    #    add_word_simple(word['en'], word['ru'])
    #    print(word['id'])



