class Normal_item():

    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        # Velocidad a la cual cambian las propiedades de Normal_item en un dia
        self.quality_speed = -1
        self.sell_in_speed = -1

    def __repr__(self):
        return "name: %s, sell_in: %s, quality: %s" % (self.name, self.sell_in, self.quality)

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

    def update_item(self):
        Normal_item.update_quality_speed(self)
        Normal_item.update_sell_in(self)
        Normal_item.update_quality(self)
        Normal_item.check_quality_limits(self)
