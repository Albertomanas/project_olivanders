from Lógica.Normal_item import Normal_item


class Aged_brie(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        # Por regla general, la quality_speed de Agred_brie será 1.
        self.quality_speed = 1

    # Aged brie, es un item que aumenta su calidad a medida que pasa el tiempo.
    # Cuando su fecha de sell_in sea menor que 0 su calidad aumentara
    # el doble de rápido

    def update_quality_speed(self):
        if self.sell_in <= 0:
            self.quality_speed = 2
        else:
            self.quality_speed = 1
