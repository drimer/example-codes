import db
import common
from common import Comment

DB_FILENAME = 'DB.sqlite'


def add_new_tables():
    sql_stmts = (
        'CREATE TABLE IF NOT EXISTS comment4 (id INT PRIMARY KEY, text TEXT)',
        'CREATE TABLE IF NOT EXISTS comment5 (id INT PRIMARY KEY, text TEXT)',
    )
    cursor = db.cursor()
    for sql in sql_stmts:
        cursor.execute(sql)


def rebalance_existing_comments():
    comments = list(Comment.get_all())
    for comment in comments:
        comment.delete()
    common.NUM_COMMENT_TABLES = 6
    for comment in comments:
        comment.save()


def main():
    with db.connect():
        add_new_tables()
        rebalance_existing_comments()


if __name__ == '__main__':
    main()
