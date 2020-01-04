from Normal_item import Normal_item


class Sulfuras_hand(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        # Item sulfuras nunca cambia sell_in y quality
        self.quality_speed = 0
        self.sell_in_speed = 0

    def __repr__(self):
        return "name:%s, sell_in:%s, quality:%s" % (self.name, self.sell_in, self.quality)

    # Funcion donde definimos las condiciones que debe cumplir backstage

    def update_item(self):
        Normal_item.update_quality(self)
        Normal_item.update_sell_in(self)
