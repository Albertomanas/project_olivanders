class Aged_brie(normal_item):
    def __init__(self, name, sell_In, quality):
        Item.__init__(self, name, sell_In, quality)

# override, sobreescribimos el valor de quality de normal_item
