from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    # Home view
    url(r'^$', 'webapp.views.home'),

    # Category structure
    url(r'^api/categories/$', 'webapp.views.api_category_structure'),

    # Category listing
    url(r'^api/list/(?P<cat_a>[^/]+)/(?P<cat_b>[^/]+)/(?P<cat_c>[^/]+)/$', 'webapp.views.api_item_list')
)
