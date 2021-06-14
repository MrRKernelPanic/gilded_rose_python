!.[GildedRose].(gilded_rose.png)

# Gilded Rose
An implementation of the Gilded Rose Kata in Python.  This attempt has used a structured class based approach based on TDD using polymorphism and inheritance to calculate the quality of goods in the store.  The shop can now deal with normal, special and conjured items as specified in the REQUIREMENTS.txt

## Requirements
[Initial Specified Requirements](REQUIREMENTS.txt)

The shop needs to be able to handle items (of varying types and varying rules) that all have 3 main characteristics ```(ItemName, Sell_in, Quality)```.  The provided initial code works but needs to now handle a new type of item ```conjured``` that does not follow the rules of most of the other items.

## Approach
The existing code works but lacks the required additonal functionality and is currently written in a difficult to understand way.

TDD will allowed me to generate a series of tests to check the functionality of the provided code.  This will help me to get a good understanding of the code and will prepare me for refactoring the exsiting coded and including the new functionality.

Initially all the calculations for updating the items quality were calculated by the shop class rather than the item class.  The requirements stated that the Item class could not be modified, however through inheritence it allowed for a 'child' classes to be created that inherited the properties of the orignial Item class.

It was then possible to create a series of tests (based upon my initial test routines for items) that allowed the update quality function to be handled by the item rather than by the store.  This initially was just emulating the orignal tests to get the desired behaviour and create a series of items that matched the requirement rules.  The newly created Item clases were, ```NormalItem, AgedItem, LegendaryItem, TicketItem``` and eventually ```ConjuredItem```.

As all the Items were based upon the original ```Item``` class they could using polymorphism having a tweaked internal function _update_quality which carried out the specific rules required for that type of item and updated the quality accordingly.  

To further reduce repetition of code I eventually based NormalItem on the original Item, and then all other child instances were based upon the ```NormalItem``` functionality which allowed calling the 'NormalItem update_item' function and reduced the sell_in count by 1 (as it would naturally run day by day) (Except for those pesky LegendaryItems where the function had to be overriden)

## Dependencies
The system was created and run and tested on Python 3.7+ using Pytest which can easily be installed using ```apt install python3-pytest``` or via pip using ```pip install -U pytest```

## Getting Started
- Clone this repo
- Navigate to the directory

## Usage
- import the gilded_rose.py

    ```from gilded_rose import GildedRose, NormalItem, AgedItem, LegendaryItem, TicketItem, ConjuredItem```

- Create a list of several items to use e.g

  ```items = [```
     ```   NormalItem("pear", 7, 5), ```
     ```   AgedItem("Aged Brie", 7, 5), ```
     ```   LegendaryItem("Sulphuras, Hand of Ragnaros", 5, 80), ```
     ```   TicketItem("Backstage passes to a TAFKAL80ETC concert", 15, 25)```
     ```   ] ```
- Create an instance of the Gilded Rose Store

    ```    gilded_rose = GildedRose(items) ```
- Run the update function to update the products sell_in and quality

    ``` gilded_rose.update_quality()```
- You can then cycle through each product in the items list checking their quality key value.
```test=items[0].quality```

## Testing
There were 23 final tests.
- Check reporting of adding a ```NormalItem```
- Check the update of a ```NormalItem```
- 4 more test on ```NormalItems``` to check boundaries / limits of ```NormalItems``` testing expect behaviour.
- 4 tests carried out on ```AgedItems``` to check adding, and daily update functionality.
- 1 test for ```LegendaryItems```
- 5 tests for ```TicketItems```
- 5 tests for ```ConjuredItems```, inital setup and them limit checks.

## Reflections
The most important part and lesson that I learnt from this was how to slowly transfer the ```update_quality``` function to within the different item classes.  Doing this slowly a class at a time based upon the parent class by running through the exact same testing process I carried out originally to test functionality.  This process meant I was not modifying the existing(working) shop functionality, just reproducing this in a more modular thorough and clear way until eventually all behaviour is emulated through the new Item classes and the orginial shop object can be altered to call each item individually and the items then handle the update themselves.