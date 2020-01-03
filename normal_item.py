class Normal_item():

    def __init__(self, name, sell_in=1, quality=1):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.quality_speed = -1
        self.sell_in_speed = -1

    def __repr__(self):
        return "name:%s, sell_in:%s, quality:%s" % (self.name, self.sell_in, self.quality)

    # def checksellinspeed i quality speed()

    def update_quality(self):
        self.quality -= 1

    def update_sell_in(self):
        self.sell_in -= 1

    # funciones para casos test

    def get_quality(self):
        return self.quality

    # def general para cambiar todo el item


if __name__ == "__main__":
    p = Normal_item("pato", 2, 2)
    q = Normal_item("kaka")
    print(p,q)
    p.update_quality()
    print(p)
    assert p.get_quality() == 1
