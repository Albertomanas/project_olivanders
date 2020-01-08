import os
from flask_sqlalchemy import SQLAlchemy
from app import app

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Inventory(db.Model):
    __tablename__ = 'Inventory'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    sell_in = db.Column(db.Integer)
    quality = db.Column(db.Integer)

    def database_to_list(self):
        query_all(self)

    def __repr__(self):
        return "%d, %s, %d, %d" % (self.id, self.name, self.sell_in, self.quality)


if __name__ == "__main__":
    Inventory.query_all()