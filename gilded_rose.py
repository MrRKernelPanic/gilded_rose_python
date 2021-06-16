# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update_item()


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class NormalItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_item(self):
        self.sell_in -= 1
        self._update_quality()

    def _update_quality(self):
        if self.sell_in <= 0:
            self.quality -= 2
        elif self.sell_in > 0:
            self.quality -= 1
        if self.quality < 0:
            self.quality = 0


class AgedItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.sell_in <= 0:
            self.quality += 2
        else:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50


class LegendaryItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def update_item(self):
        pass


class TicketItem(NormalItem):
    def __init__(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <= 5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        else:
            self.quality += 1


class ConjuredItem(NormalItem):
    def __init(self, name, sell_in, quality):
        NormalItem.__init__(self, name, sell_in, quality)

    def _update_quality(self):
        if self.sell_in >= 0:
            self.quality -= 2
        else:
            self.quality -= 4
        if self.quality < 0:
            self.quality = 0
