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


if __name__ == "__main__":
    items = Gilded_rose([
            Conjured("+5 Dexterity Vest", 10, 20),
            Aged_brie("Aged Brie", 2, 0),
            Normal_item("Elixir of the Mongoose", 5, 7),
            Sulfuras_hand("Sulfuras, Hand of Ragnaros", 0, 80),
            Sulfuras_hand("Sulfuras, Hand of Ragnaros", -1, 80),
            Backstage_pass("Backstage passes to a TAFKAL80ETC concert", 15, 20),
            Backstage_pass("Backstage passes to a TAFKAL80ETC concert", 10, 49),
            Backstage_pass("Backstage passes to a TAFKAL80ETC concert", 5, 49),
            Conjured("Conjured Mana Cake", 3, 6)])
    items.update_items()
    items_updated = Gilded_rose([
            Conjured("+5 Dexterity Vest", 9, 18),
            Aged_brie("Aged Brie", 1, 1),
            Normal_item("Elixir of the Mongoose", 4, 6),
            Sulfuras_hand("Sulfuras, Hand of Ragnaros", 0, 80),
            Sulfuras_hand("Sulfuras, Hand of Ragnaros", -1, 80),
            Backstage_pass("Backstage passes to a TAFKAL80ETC concert", 14, 21),
            Backstage_pass("Backstage passes to a TAFKAL80ETC concert", 9, 50),
            Backstage_pass("Backstage passes to a TAFKAL80ETC concert", 4, 50),
            Conjured("Conjured Mana Cake", 2, 4)])
    print(items.get_items())
    print(items_updated.get_items())
