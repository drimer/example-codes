from django.conf.urls import url, include

from people import urls as people_urls

urlpatterns = [
    url(r'^', include(people_urls)),
]
