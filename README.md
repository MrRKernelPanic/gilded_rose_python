![GildedRose](gilded_rose.png)

# Gilded Rose
An implementation of the Gilded Rose Kata in Python.  This attempt has used a structured class approach based on TDD using polymorphism and inheritance to calculate the quality of goods in the store.  The shop can now deal with normal, special and conjured items as specified in the REQUIREMENTS.txt

## Requirements
[Initial Specified Requirements](REQUIREMENTS.txt)

The shop needs to be able to handle items (of varying types and varying rules) that all have 3 main characteristics ```(ItemName, Sell_in, Quality)```.  The provided initial code worked but now needs to handle a new type of item ```conjured``` this does not follow the rules of most other items.

## Approach
The existing code worked but lacked the required additonal functionality was currently written in a difficult to understand way.

TDD allowed me to generate a series of tests to check the functionality of the provided code.  This helped me to get a good understanding of the code and prepared me for refactoring the exsiting code and including the new functionality.

Initially all the calculations for updating the items quality were calculated by the shop class rather than the item class.  The requirements stated that the ```Item``` class could not be modified, however through inheritence it allowed for a 'child' classes to be created that inherited the properties of the orignial Item class.

It then became possible to create a series of tests (based upon my initial test routines for the different items) that allowed the ```update_quality``` function to be handled by the item rather than by the store.  This initially was just emulating the orignal tests to get the desired behaviour and then create a series of items that matched the requirement rules.  The newly created Item clases were, ```NormalItem, AgedItem, LegendaryItem, TicketItem``` and eventually ```ConjuredItem```.

As all the Items were based upon the original ```Item``` class they could use polymorphism having a tweaked internal function _update_quality which carried out the specific rules required for that type of item and would update the quality accordingly.  

To further reduce repetition of code I eventually based NormalItem on the original Item, and then all other child instances were based upon the ```NormalItem```.  This functionality allowed calling the 'NormalItem update_item' function and reduced the sell_in count by 1 (as it would naturally run day by day) (Except for those pesky LegendaryItems where the function had to be overriden)

## Dependencies
The system was created and run and tested on Python 3.8+ using Pytest which can easily be installed using ```apt install python3-pytest``` or via pip using ```pip install -U pytest```

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
There were 23 final tests.  Which can be run from the console using pytest.  The tests were finally split into several files, one for each type of item (as indicated in the test filenames)
- Check reporting of adding a ```NormalItem``` can be foundin the gilded_rose_test.  These seven tests check the expected outcomes for adding an item, test normal update, testing the quality cannot go below zero, testing the item quality after the sell_in date has passed, testing the quality after the sell_in date has passed and the quality is already zero and finally a test that included the various different types of items.
- 4 tests carried out on ```AgedItems``` to check adding, and daily update functionality.
- 1 test for ```LegendaryItems``` to check that quality and sell_in date never change.
- 5 tests for ```TicketItems``` to check how fast they increase in quality in relation to the sell_in date, and that their quality drops to zero the day after the concert.
- 5 tests for ```ConjuredItems```, inital setup and them limit checks.

## Reflections
The most important part and lesson that I learnt from this was how to slowly transfer the ```update_quality``` function to within the different item classes.  Doing this slowly a class at a time based upon the parent class by running through the exact same testing process I carried out originally to test functionality.  This process meant I was not modifying the existing(working) shop functionality, just reproducing this in a more modular thorough and clear way until eventually all behaviour is emulated through the new Item classes and the orginial shop object can be altered to call each item individually and the items then handle the update themselves.  I also learnt that it is possible and sensible to split testing up into individual items to make more readable, managable and easier to find.  This was also my first experience of using a python linter (PycodeStyle to match PEP8 syntax)
