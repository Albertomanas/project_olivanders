from Item import Item
from updatable import updatable


class Normal_item(Item, updatable):

    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
        # Velocidad a la cual cambian las propiedades de Normal_item en un dia
        self.quality_speed = -1
        self.sell_in_speed = -1

    # Propiedades básicas de quality y sell_in

    def update_quality(self):
        self.quality += self.quality_speed

    def update_sell_in(self):
        self.sell_in += self.sell_in_speed

    # Funciones para poder comprobar datos en los casos test

    def get_quality(self):
        return self.quality

    def get_sell_in(self):
        return self.sell_in

    def get_item_updated(self):
        return self.name, self.sell_in, self.quality

    # Funcion donde definimos las condiciones que debe cumplir

    def check_quality_limits(self):
        if self.quality <= 0:
            self.quality = 0
        elif self.quality > 50:
            self.quality = 50

    def update_quality_speed(self):
        if self.sell_in <= 0:
            self.quality_speed = -2
        else:
            self.quality_speed = -1

    # Las funciones de update item, deben seguir
    # el siguiente orden para su correcto funcionamiento

    def update_item(self):
        # actualizamos la velocidad de variación de quality depende de sell_in
        # siempre debera ir primera
        self.update_quality_speed()
        # no importan el orden de update_sell_in, ni de update_quality
        self.update_sell_in()
        self.update_quality()
        # check quality limits siempre debera ir el ultimo de todos
        self.check_quality_limits()
