import db

NUM_COMMENT_TABLES = 4


class Comment(object):

    last_id = 0

    def __init__(self, text, id=None):
        self.id = id or Comment.new_id()
        self.text = text

    def save(self):
        table_name = Comment.get_table_name(self.id)
        cursor = db.cursor()
        cursor.execute(
            "INSERT INTO %s(id, text) values (%s, '%s')" % (
                table_name, self.id, self.text
            )
        )

    def delete(self):
        table_name = Comment.get_table_name(self.id)
        cursor = db.cursor()
        cursor.execute(
            "DELETE FROM %s where id = %s and text = '%s'" % (
                table_name, self.id, self.text
            )
        )

    @staticmethod
    def get_object_by_id(id):
        table_name = Comment.get_table_name(id)
        cursor = db.cursor()
        db_res = cursor.execute(
            "SELECT id, text from %s where id = %s" % (
                table_name, id
            )
        )
        try:
            dbr = db_res.next()
        except StopIteration:
            return None

        return Comment(dbr[1], id=dbr[0])


    @staticmethod
    def get_all():
        tables = ['comment%s' % i for i in range(NUM_COMMENT_TABLES)]
        cursor = db.cursor()
        for table in tables:
            db_res = cursor.execute(
                "SELECT id, text from %s;" % table
            )
            for dbr in db_res:
                yield Comment(dbr[1], id=dbr[0])


    @staticmethod
    def new_id():
        tables = ['comment%s' % i for i in range(NUM_COMMENT_TABLES)]
        cursor = db.cursor()
        db_res = [
            cursor.execute("SELECT max(id) from %s" % table).next()
            for table in tables
        ]
        max_id = max([rs[0] if rs[0] else 0 for rs in db_res])
        return max_id + 1

    @staticmethod
    def get_table_name(id):
        id_hashed = id % NUM_COMMENT_TABLES
        table_name = 'comment%s' % id_hashed
        return table_name
