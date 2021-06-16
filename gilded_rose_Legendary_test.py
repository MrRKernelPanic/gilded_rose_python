import pytest

from gilded_rose import GildedRose, LegendaryItem


def test_legendary_item_sulfuras_quality_and_sell_in_never_chage():
    item = LegendaryItem("Sulphuras, Hand of Ragnaros", 5, 80)
    item.update_item()
    assert item.quality == 80
    assert item.sell_in == 5
