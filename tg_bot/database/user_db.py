from peewee import SqliteDatabase, Model, CharField, IntegerField

db = SqliteDatabase("user_db.db")

class User(Model):
    name = CharField()

    class Meta:
        database = db

db.create_tables([User])

