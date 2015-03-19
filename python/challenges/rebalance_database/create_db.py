import random

import db
from common import Comment

NUM_RANDOM_COMMENTS = 20


def create_schema():
    sql_stmts = (
        'CREATE TABLE IF NOT EXISTS comment0 (id INT PRIMARY KEY, text TEXT)',
        'CREATE TABLE IF NOT EXISTS comment1 (id INT PRIMARY KEY, text TEXT)',
        'CREATE TABLE IF NOT EXISTS comment2 (id INT PRIMARY KEY, text TEXT)',
        'CREATE TABLE IF NOT EXISTS comment3 (id INT PRIMARY KEY, text TEXT)',
    )
    cursor = db.cursor()
    for sql in sql_stmts:
        cursor.execute(sql)


def get_random_text():
    all_texts = (
        'There will be a DB** with Comments.',
        'The object Comment (id = number, text = string)',
        'will provide save() and get_object_by_id(id=[number])',
        'methods, which saves and retrieves the object from a DB**',
        '(see notes below).Every object will be saved in one of',
        '4 tables (tables have the same structure and named like',
        'comment0, comment1, comment2, comment3) depending on the',
        'object id using the Modulus function:',
        'ID % 4 = 0, 1, 2, or 3.',
    )
    return random.choice(all_texts)


def populate_with_random_comments():
    for _ in range(NUM_RANDOM_COMMENTS):
        text = get_random_text()
        comment = Comment(text)
        comment.save()


def main():
    with db.connect():
        create_schema()
        populate_with_random_comments()


if __name__ == '__main__':
    main()
