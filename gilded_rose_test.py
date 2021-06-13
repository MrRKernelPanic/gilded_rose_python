import pytest

from gilded_rose import GildedRose, NormalItem, AgedItem, LegendaryItem, TicketItem, ConjuredItem

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

def test_legendary_item_sulfuras_quality_and_sell_in_never_chage():
    item = LegendaryItem("Sulphuras, Hand of Ragnaros", 5, 80)
    item.update_item()
    assert item.quality == 80
    assert item.sell_in == 5

def test_ticket_item_backstage_pass_normal_quality_increase():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 15,25)
    item.update_item()
    assert item.quality == 26

def test_ticket_item_backstage_pass_ten_or_less_sell_in():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 9 ,25)
    item.update_item()
    assert item.quality == 27

def test_ticket_item_backstage_pass_five_or_less_sell_in():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 5, 25)
    item.update_item()
    assert item.quality == 28

def test_ticket_item_backstage_pass_quality_after_sell_in_zero():
    item = TicketItem("Backstage passes to a a TAFKAL80ETC concert", 0 ,25)
    item.update_item()
    assert item.quality == 0

def test_ticket_item_backstage_pass_one_sell_in():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 1 ,25)
    item.update_item()
    assert item.quality == 28    

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
