from json import dumps

from django.http.response import HttpResponse
from django.shortcuts import render

from webapp.categories import CATEGORIES


__author__ = 'shillaker'


# Home view
def home(request):
    return render(request, 'home.html')


# Category structure API
def api_category_structure(request):
    categories_json = dumps(CATEGORIES)
    return HttpResponse(categories_json, content_type='application/json')


# Category contents API
def api_item_list(request, cat_a, cat_b, cat_c):
    items_list = CATEGORIES[cat_a][cat_b][cat_c]
    items_list_json = dumps(items_list)
    return HttpResponse(items_list_json, content_type='application/json')
