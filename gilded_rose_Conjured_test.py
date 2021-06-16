import pytest

from gilded_rose import GildedRose, ConjuredItem


def test_conjured_item():
    item = ConjuredItem("Summon Shirt", 5, 10)
    assert "Summon Shirt, 5, 10" == item.__repr__()


def test_update_item_conjured():
    item = ConjuredItem("Pear", 7, 5)
    item.update_item()
    assert item.quality == 3


def test_conjured_item_quality_cannot_go_below_zero():
    item = ConjuredItem("Pear", 7, 0)
    item.update_item()
    assert item.quality == 0


def test_conjured_item_quality_after_sell_date_passed():
    item = ConjuredItem("Pear", 0, 5)
    item.update_item()
    assert item.quality == 1


def test_conjured_item_quality_after_sell_date_passed_and_quality_is_zero():
    item = ConjuredItem("Pear", 0, 0)
    item.update_item()
    assert item.quality == 0


def test_conjured_item_quality_after_sell_date_passed_and_quality_is_one():
    item = ConjuredItem("Pear", 1, 1)
    item.update_item()
    assert item.quality == 0
