# -*- coding: utf-8 -*-
import pytest

from gilded_rose import GildedRose, Item, NormalItem, AgedItem

def test_item():
    item = Item("Apple", 5, 10)
    assert "Apple, 5, 10" == item.__repr__()

def test_add_to_store():
    item = Item("Pear", 7, 5)
    gilded_rose = GildedRose([item])
    assert gilded_rose.items[0].name == "Pear"
    assert gilded_rose.items[0].sell_in == 7
    assert gilded_rose.items[0].quality == 5

def test_update_quality():
    item = Item("Pear", 7, 5)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 4
    assert gilded_rose.items[0].sell_in == 6

def test_update_quality_lowest_possible_value():
    item = Item("Pear", 7, 0)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0

def test_quality_after_sell_date_passed():
    item = Item("Pear", 0, 5)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 3

def test_aged_brie_quality_increases_with_age():
    item = Item("Aged Brie", 1, 5)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 6    

def test_aged_brie_quality_increases_twice_as_fast_past_sell_in_less_than_zero():
    item = Item("Aged Brie", 0, 5)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 7

def test_quality_never_increases_over_fifty():
    item = Item("Aged Brie", 0, 50)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 50

def test_sulfuras_quality_and_sell_in_never_change():
    item = Item("Sulfuras, Hand of Ragnaros", 5, 80)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 80
    assert gilded_rose.items[0].sell_in == 5

def test_backstage_pass_quality_normal_increase():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 15, 25)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 26

def test_backstage_pass_quality_ten_or_less_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 9, 25)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 27

def test_backstage_pass_quality_three_or_less_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 5, 25)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 28

def test_backstage_pass_quality_after_sell_in():
    item = Item("Backstage passes to a TAFKAL80ETC concert", 0, 25)
    gilded_rose = GildedRose([item])
    gilded_rose.update_quality()
    assert gilded_rose.items[0].quality == 0

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

def test_brie_item():
    item = AgedItem("Aged Brie", 5, 10)
    assert "Aged Brie, 5, 10" == item.__repr__()

def test_update_aged_item_brie_quality():
    item = AgedItem("Aged Brie", 7, 5)
    item.update_item()
    assert item.sell_in == 6
    assert item.quality == 6

def test_update_aged_item_brie_quality_increases_twice_as_fast_past_sell_in_zero():
    item = AgedItem("Aged Brie", 0, 5)
    item.update_item()
    assert item.quality == 7

def test_aged_item_brie_quality_never_above_fifty():
    item = AgedItem("Aged Brie", 0, 50)
    item.update_item()
    assert item.quality == 50
