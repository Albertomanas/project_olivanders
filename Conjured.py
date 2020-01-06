from Normal_item import Normal_item


class Conjured(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        self.quality_speed = -2


def update_quality_speed(self):
    if self.sell_in <= 0:
        self.quality_speed = -4
    else:
        self.quality_speed = -2


def update_item(self):
    Conjured.update_quality_speed(self)
    Normal_item.update_quality(self)
    Normal_item.update_sell_in(self)
    Normal_item.check_quality_limits(self)
