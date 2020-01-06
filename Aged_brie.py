from Normal_item import Normal_item


class Aged_brie(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        # Por regla general, la quality_speed de Agred_brie será 1.
        self.quality_speed = 1

    def update_quality_speed(self):
        if self.sell_in <= 0:
            self.quality_speed = 2
        else:
            self.quality_speed = 1

    def update_item(self):
        Aged_brie.update_quality_speed(self)
        Normal_item.update_quality(self)
        Normal_item.update_sell_in(self)
        Normal_item.check_quality_limits(self)