from Normal_item import Normal_item


class Backstage_pass(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        # Velocidad estandard de backstage, gana calidad
        self.quality_speed = 1

    def __repr__(self):
        return "name:%s, sell_in:%s, quality:%s" % (self.name, self.sell_in, self.quality)

    # Funcion donde definimos las condiciones que debe cumplir backstage

    def update_quality_speed(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality_speed = 5
        elif self.sell_in <= 10:
            self.quality = 2
        else:
            self.quality_speed = 1

    def update_item(self):
        Backstage_pass.update_quality_speed(self)
        Normal_item.update_quality(self)
        Normal_item.update_sell_in(self)
