# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                if item.quality > 0:
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        item.quality = item.quality - 1
            else:
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        if item.sell_in < 11:
                            if item.quality < 50:
                                item.quality = item.quality + 1
                        if item.sell_in < 6:
                            if item.quality < 50:
                                item.quality = item.quality + 1
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in = item.sell_in - 1
            if item.sell_in < 0:
                if item.name != "Aged Brie":
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        if item.quality > 0:
                            if item.name != "Sulfuras, Hand of Ragnaros":
                                item.quality = item.quality - 1
                    else:
                        item.quality = item.quality - item.quality
                else:
                    if item.quality < 50:
                        item.quality = item.quality + 1



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

class AgedItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_item(self):
        self.sell_in -= 1
        self._update_quality()

    def _update_quality(self):
        if self.sell_in <= 0:
            self.quality += 2
        else:
            self.quality += 1
        if self.quality > 50:
            self.quality = 50

class LegendaryItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)

    def update_item(self):
        pass

class TicketItem(Item):
    def __init__(self, name, sell_in, quality):
        Item.__init__(self, name, sell_in, quality)
    
    def update_item(self):
        self.sell_in -= 1
        self._update_quality()

    def _update_quality(self):
        if self.sell_in < 0:
            self.quality = 0
        elif self.sell_in <=5:
            self.quality += 3
        elif self.sell_in <= 10:
            self.quality += 2
        elif self.quality > 0:
            self.quality += 1
