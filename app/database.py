import os
from flask_sqlalchemy import SQLAlchemy
from app import app
from Lógica.Normal_item import Normal_item
from Lógica.Aged_brie import Aged_brie
from Lógica.Backstage_pass import Backstage_pass
from Lógica.Conjured import Conjured
from Lógica.Sulfuras_hand import Sulfuras_hand


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

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    @staticmethod
    def get_all():
        return Inventory.query.all()

    @staticmethod
    def get_by_id(id):
        return Inventory.query.get(id)

    # no se si es correcto escribir esta funcion aqui

    @staticmethod
    def all_query_to_filtred_list():

        items_for_gilded = []

        dexterity = str(Inventory.query.get(1))
        dexterity = dexterity.split(',')
        if dexterity[0] == "+5 Dexterity Vest":
            items_for_gilded.append(Normal_item(
                dexterity[0], int(dexterity[1]), int(dexterity[2])))

        aged_brie = str(Inventory.query.get(2))
        aged_brie = aged_brie.split(',')
        if aged_brie[0] == "Aged Brie":
            items_for_gilded.append(
                Aged_brie(aged_brie[0], int(aged_brie[1]), int(aged_brie[2])))

        moogoose = str(Inventory.query.get(3))
        moogoose = moogoose.split(',')
        if moogoose[0] == "Elixir of the Mongoose":
            items_for_gilded.append(Normal_item(
                moogoose[0], int(moogoose[1]), int(moogoose[2])))

        sulfuras = str(Inventory.query.get(4))
        sulfuras = sulfuras.split(',')
        if sulfuras[0] == "Sulfuras":
            items_for_gilded.append(Sulfuras_hand(
                (sulfuras[0] + "," + sulfuras[1]), int(sulfuras[2]), int(sulfuras[3])))

        sulfuras = str(Inventory.query.get(5))
        sulfuras = sulfuras.split(',')
        if sulfuras[0] == "Sulfuras":
            items_for_gilded.append(Sulfuras_hand(
                (sulfuras[0] + "," + sulfuras[1]), int(sulfuras[2]), int(sulfuras[3])))

        backstage = str(Inventory.query.get(6))
        backstage = backstage.split(',')
        if backstage[0] == "Backstage passes to a TAFKAL80ETC concert":
            items_for_gilded.append(Backstage_pass(
                backstage[0], int(backstage[1]), int(backstage[2])))

        backstage = str(Inventory.query.get(7))
        backstage = backstage.split(',')
        if backstage[0] == "Backstage passes to a TAFKAL80ETC concert":
            items_for_gilded.append(Backstage_pass(
                backstage[0], int(backstage[1]), int(backstage[2])))

        backstage = str(Inventory.query.get(8))
        backstage = backstage.split(',')
        if backstage[0] == "Backstage passes to a TAFKAL80ETC concert":
            items_for_gilded.append(Backstage_pass(
                backstage[0], int(backstage[1]), int(backstage[2])))

        conjured = str(Inventory.query.get(9))
        conjured = conjured.split(',')
        if conjured[0] == "Conjured Mana Cake":
            items_for_gilded.append(
                Conjured(conjured[0], int(conjured[1]), int(conjured[2])))

        return items_for_gilded
