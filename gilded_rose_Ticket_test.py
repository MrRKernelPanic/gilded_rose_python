import pytest

from gilded_rose import GildedRose, TicketItem


def test_ticket_item_backstage_pass_normal_quality_increase():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 15, 25)
    item.update_item()
    assert item.quality == 26


def test_ticket_item_backstage_pass_ten_or_less_sell_in():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 9, 25)
    item.update_item()
    assert item.quality == 27


def test_ticket_item_backstage_pass_five_or_less_sell_in():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 5, 25)
    item.update_item()
    assert item.quality == 28


def test_ticket_item_backstage_pass_quality_after_sell_in_zero():
    item = TicketItem("Backstage passes to a a TAFKAL80ETC concert", 0, 25)
    item.update_item()
    assert item.quality == 0


def test_ticket_item_backstage_pass_one_sell_in():
    item = TicketItem("Backstage passes to a TAFKAL80ETC concert", 1, 25)
    item.update_item()
    assert item.quality == 28
