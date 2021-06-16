import pytest

from gilded_rose import GildedRose, AgedItem


def test_brie_item():
    item = AgedItem("Aged Brie", 5, 10)
    assert "Aged Brie, 5, 10" == item.__repr__()


def test_update_aged_item_brie_quality():
    item = AgedItem("Aged Brie", 7, 5)
    item.update_item()
    assert item.sell_in == 6
    assert item.quality == 6


def test_update_aged_item_brie_quality_increase_2x_as_fast_past_sell_in_zero():
    item = AgedItem("Aged Brie", 0, 5)
    item.update_item()
    assert item.quality == 7


def test_aged_item_brie_quality_never_above_fifty():
    item = AgedItem("Aged Brie", 0, 50)
    item.update_item()
    assert item.quality == 50
