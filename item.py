class Item:
    def __init__(self, name, sell_In, quality):
        self.name = name
        self.sell_In = sell_In
        self.quality = quality
# Coje de una string name, sellIn y quality

    def __repr__(self):
        return "name:%s, sell_in:%s, quality:%s" % (self.name, self.sell_In, self.quality)