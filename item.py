class Item:
    def __init__(self, name, sellIn, quality):
        self.name = name
        self.sellIn = sellIn
        self.quality = quality
# Coje de una string name, sellIn y quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sellIn, self.quality)
