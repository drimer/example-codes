from random import randint, choice

__author__ = 'shillaker'


# Builds some random items
def _build_items(category_name):
    n_items = randint(0, 10)
    items_list = list()
    for x in range(0, n_items):
        this_price = randint(0, 2000) / 100.0
        this_id = randint(0, 1000000)
        items_list.append({
            'id': this_id,
            'price': this_price,
            'description': _generate_random_description(category_name)
        })

    return items_list


_adjectives = ['lovely', 'goregeous', 'antique', 'stately', 'kitsch', 'shabby chic']
_periods = ['georgian', 'modern', 'retro', 'bauhaus', 'ultra modern', 'victorian']


# Generates a random description
def _generate_random_description(category_name):
    category_name_singular = category_name[:-1]
    return '%s %s %s' % (choice(_adjectives), choice(_periods), category_name_singular)


# Main category structure
CATEGORIES = {
    'bedroom': {
        'beds': {
            'single beds': _build_items('single beds'),
            'double beds': _build_items('double beds'),
            'sofa beds': _build_items('sofa beds')
        },
        'bedding': {
            'duvets': _build_items('duvets'),
            'pillows': _build_items('pillows'),
            'sheets': _build_items('sheets')
        },
        'mattresses': {
            'single mattresses': _build_items('single mattresses'),
            'double mattresses': _build_items('double mattresses'),
            'childrens mattresses': _build_items('childrens mattresses')
        },
        'mirrors': {
            'free standing mirrors': _build_items('free standing mirrors'),
            'wall mirrors': _build_items('wall mirrors')
        }
    },
    'living room': {
        'curtains': {
            'curtain fabrics': _build_items('curtain fabrics'),
            'curtain poles': _build_items('curtain poles'),
            'curtain tassles': _build_items('curtain tassles'),
        },
        'sofas': {
            'one seaters': _build_items('one seaters'),
            'two seaters': _build_items('two seaters'),
            'three seaters': _build_items('three seaters')
        },
        'tables': {
            'coffee tables': _build_items('coffee tables'),
            'console tables': _build_items('console tables'),
            'side tables': _build_items('side tables'),
        },
    },
    'office': {
        'seating': {
            'desk chairs': _build_items('desk chairs'),
            'meeting room chairs': _build_items('meeting room chairs')
        },
        'storage': {
            'bookcases': _build_items('bookcases'),
            'filing cabinets': _build_items('filing cabinets'),
            'pedestals': _build_items('pedestals')
        }
    },
    'outdoor': {
        'seating': {
            'deck chairs': _build_items('deck chairs'),
            'benches': _build_items('benches'),
            'plastic chairs': _build_items('plastic chairs')
        }
    },
}




