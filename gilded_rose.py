from Item import Item
from Normal_item import Normal_item
from Aged_brie import Aged_brie
from Backstage_pass import Backstage_pass
from Conjured import Conjured
from Sulfuras_hand import Sulfuras_hand

# barricada para pasar solo los datos necesarios


class Gilded_rose(object):
    def __init__(self, items):
        self.items = items
        # .updatable

    def update_items(self):
        for item in self.items:
            name = Gilded_rose.name_item_for_update(item)
            sell_in = Gilded_rose.sell_in_item_for_update(item)
            quality = Gilded_rose.quality_item_for_update(item)
            itemized = Normal_item(name, sell_in, quality)
            itemized.update_item()
            item = itemized
        return self.items

    def get_items_updated(self):
        return self.items

    @staticmethod
    def name_item_for_update(item):
        contador = 1
        while contador <= 3:
            for i in item:
                if contador == 1:
                    name = i
            contador += 1
        return name

    @staticmethod
    def sell_in_item_for_update(item):
        contador = 1
        while contador <= 3:
            for i in item:
                if contador == 2:
                    sell_in = i
            contador += 1
        return sell_in

    @staticmethod
    def quality_item_for_update(item):
        contador = 1
        while contador <= 3:
            for i in item:
                if contador == 3:
                    quality = i
            contador += 1
        return quality


if __name__ == "__main__":
    pato = Gilded_rose([["pato", 2, 0], ["pato", 2, 0]])
    pato.update_items()
    print(pato.get_items_updated()) # == ([["pato", 1, 0], ["pato", 1, 0]])
