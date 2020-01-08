from Lógica.Item import Item
from Lógica.Normal_item import Normal_item
from Lógica.Aged_brie import Aged_brie
from Lógica.Backstage_pass import Backstage_pass
from Lógica.Conjured import Conjured
from Lógica.Sulfuras_hand import Sulfuras_hand

# barricada para pasar solo los datos necesarios


class Gilded_rose(object):
    def __init__(self, items, days):
        self.items = items
        self.days = days
        # .updatable

    def update_items(self):
        for day in range(1, self.days + 1):
            for item in self.items:
                item.update_item()

    def get_items(self):
        return self.items

    def __repr__(self):
        return "%s" % (self.items)

    def main(self):
        self.update_items()
        self.get_items()
