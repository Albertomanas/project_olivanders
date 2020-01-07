from Normal_item import Normal_item

# En conjured, los items perderan el doble de
# calidad a medida que pase el tiempo


class Conjured(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        self.quality_speed = -2

    # Perderan el doble de rápido que normal ítem

    def update_quality_speed(self):
        if self.sell_in <= 0:
            self.quality_speed = -4
        else:
            self.quality_speed = -2
