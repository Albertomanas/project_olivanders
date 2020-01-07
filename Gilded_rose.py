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
            item.update_item()

    def get_items(self):
        return self.items

    def __eq__(self, items_updated):
        return self.__dict__ == items_updated.__dict__

    def equals(self, update_items):
        i = 0
        while(i < len(update_items.get_items())):
            if str(update_items.get_items()[i]) == str(self.get_items()[i]):
                pass
            else:
                return False
            i += 1
        return True
    # preguntar a david
