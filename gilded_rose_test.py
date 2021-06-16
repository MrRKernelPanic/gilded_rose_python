import pytest

from gilded_rose import GildedRose
from gilded_rose import NormalItem, AgedItem, LegendaryItem, TicketItem
from gilded_rose import ConjuredItem


def test_normal_item():
    item = NormalItem("Apple", 5, 10)
    assert "Apple, 5, 10" == item.__repr__()


def test_update_normal_item_quality():
    item = NormalItem("Pear", 7, 5)
    item.update_item()
    assert item.sell_in == 6
    assert item.quality == 4


def test_normal_item_quality_cannot_go_below_zero():
    item = NormalItem("Pear", 7, 0)
    item.update_item()
    assert item.quality == 0


def test_normal_item_quality_after_sell_date_passed():
    item = NormalItem("Pear", 0, 5)
    item.update_item()
    assert item.quality == 3


def test_normal_item_quality_after_sell_date_passed_and_quality_is_zero():
    item = NormalItem("Pear", 0, 0)
    item.update_item()
    assert item.quality == 0


def test_normal_item_quality_after_sell_date_passed_and_quality_is_one():
    item = NormalItem("Pear", 1, 1)
    item.update_item()
    assert item.quality == 0


def test_gilded_rose_shop_one_of_each_item_type():
    items = [
        NormalItem("pear", 7, 5),
        AgedItem("Aged Brie", 7, 5),
        LegendaryItem("Sulphuras, Hand of Ragnaros", 5, 80),
        TicketItem("Backstage passes to a TAFKAL80ETC concert", 15, 25)
        ]
    gilded_rose = GildedRose(items)
    gilded_rose.update_quality()
    assert items[0].quality == 4
    assert items[1].quality == 6
    assert items[2].quality == 80
    assert items[3].quality == 26
