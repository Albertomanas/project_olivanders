from Lógica.Normal_item import Normal_item


class Sulfuras_hand(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        # Item sulfuras nunca cambia sell_in y quality
        self.quality_speed = 0
        self.sell_in_speed = 0

    # La calidad de sulfuras siempre debera ser 80
    def check_quality_limits(self):
        if self.quality != 80:
            self.quality = 80
