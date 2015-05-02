# Introduction

The aim of this assignment is to build a UI for navigating a catalogue of items.
 
These items are categorised in a hierarchical structure.

The UI should render this hierarchical structure in three lists that the user can choose from. Selections in the final
list should cause the table of items to populate (see the wireframe below).

A skeleton Django app is provided with JSON API endpoints for accessing the categories and lists of items.

# Running the Code

The code is contained in a vanilla Django project so can be run however you normally run Django projects.
A `start_server.sh` script is included which will start the server running at `http://localhost:8000`.

# Category Structure

The category structure has three levels:

* category A - high-level grouping of items, e.g. bedroom or living room
* category B - sub-categories of category A, slightly narrower groupings of items e.g. tables, sofas etc. 
* category C - very specific categories of items e.g. coffee tables, one seater sofas etc.

Each item in the catalogue belongs to a single category C. The aim of the UI is to allow the user to view lists of 
items based on their category C.

This is best shown with a couple of examples:

| Category A | Category B | Category C | Items |
| --- | --- | --- | --- |
| bedroom | beds | single beds | <single bed 1> | 
| | | | <single bed 2> | 
| | | | <single bed 3> | 
| | | | ... | 
| | | double beds | <double bed 1> | 
| | | | <double bed 2> | 
| | | | <double bed 3> | 
| | | | ... | 
| bedroom | bedding | duvets | <duvet a> | 
| | | | <duvet b> | 
| | | | ... | 
| | | pillows | <pillow a> | 
| | | | <pillow b> |
| | | | ... |
| living room | tables | coffee tables | <coffee table a> |
| | | | <coffee table b> |
| | | | <coffee table c> |
| | | | ... |

# Wireframe

A wireframe sketch can be found at `resources/wireframe.jpg`.

Essentially the interface should work like this:

* the user should be shown three lists to start off with
* initially only the "Category A" list is populated
* when a user selects a "Category A" item, it is highlighted and the "Category B" list is populated
* when a user selects a "Category B" item, the "Category C" list is populated
* when a user selects a "Category C" item, a table below the lists is populated with the items from that category

# API

The api has two endpoints:

## Category Structure: `/api/categories/`

The `/api/categories/` endpoint returns the hierarchical category structure as nested JSON objects. To see this structure
in more detail have a look in `webapp/categories.py`.

## Category Items: `/api/list/<category_a>/<category_b>/<category_c>/`

The URL for this endpoint needs to be constructed based on the user's selections. For example, if the user has selected
`bedroom` -> `beds` -> `single beds` the URL would look like:

    http://localhost:8000/api/list/bedroom/beds/single%20beds/

And if they had selected `living room` -> `tables` -> `coffee tables` the URL would look like:

    http://localhost:8000/api/list/living%20room/tables/coffee%20tables/
    
The response from this endpoint will be a list of JSON objects, each of which has the following properties:

* ID - a numeric ID
* price - the price of the item
* description - a brief description
