# -*- coding: utf-8 -*-
import pytest

from gilded_rose import Item, GildedRose

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
    