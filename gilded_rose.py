from item import Item


class gilded_rose(object):
    def __init__(self, items):
        self.items = items #.updatable

    def update_item(self):
        for item in self.items:
            item.update_item(self)
            #hace falta apuntar self?