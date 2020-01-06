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
            Normal_item.update_item(item)
            # hace falta apuntar self ?

    def get_items_updated(self):
        return self.items


if __name__ == "__main__":
    pato = Gilded_rose('"pato", 2, 0')
    pato.update_items()
    assert pato.get_items_updated() == (("pato", 1, 0))
