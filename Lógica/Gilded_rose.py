from Item import Item
from Normal_item import Normal_item
from Aged_brie import Aged_brie
from Backstage_pass import Backstage_pass
from Conjured import Conjured
from Sulfuras_hand import Sulfuras_hand

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
        Conjured("Conjured Mana Cake", 3, 6)], 30)
    items.update_items()
    print(items.get_items())
