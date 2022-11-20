from playhouse.db_url import connect
from peewee import Model, IntegerField, CharField
from flask_login import UserMixin

db = connect("sqlite:///peewee_db.sqlite")

if not db.connect():
    print("connection error")
    exit()
print("connection success")


class User(UserMixin, Model):
    id = IntegerField(primary_key=True)
    name = CharField()
    password = CharField()

    class Meta:
        database = db
        table_name = "user"


db.create_tables([User])
