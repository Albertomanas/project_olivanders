class Normal_item(Item, Updatable):
    # Hereda de Item y Updatable
    def __init__(self, name, sell_In, quality):
        Item.__init__(self, name, sell_In, quality)

    def set_sell_In(self):
        self.set_sell_In = self.set_sell_In - 1
# Límites de la calidad,

    def set_quality(self):
        if self.quality > 50:
            self.quality = 50   # Límite a 50
        elif self.quality <= 0:
            self.quality = 0  # Límite a 0
        else self.quality = 0

# Override del @abstractmethod de Updatable
    def update_quality(self):
        if self.sell_In > 0:
            self.set_quality(-1)
        else:
            self.quality(-2)
        self.set_sell_In()
