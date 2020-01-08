from Lógica.Normal_item import Normal_item

# El backstage pass son pases para un concierto


class Backstage_pass(Normal_item):
    def __init__(self, name, sell_in, quality):
        Normal_item.__init__(self, name, sell_in, quality)
        # Velocidad estandard de backstage, gana calidad
        self.quality_speed = 1

    # Las condiciones que debe cumplir backstage son las siguientes:
    # La calidad del pase aumentara siempre hasta llegar el dia del concierto,
    # que cuando pase, sera 0. Cuando queden menos de 10 dias, aumentara 2, 
    # cuando queden menos de 5, aumentara 5

    def update_quality_speed(self):
        if self.sell_in <= 0:
            self.quality = 0
            self.quality_speed = 0
        elif self.sell_in <= 5:
            self.quality_speed = 5
        elif self.sell_in <= 10:
            self.quality_speed = 2
        else:
            self.quality_speed = 1
