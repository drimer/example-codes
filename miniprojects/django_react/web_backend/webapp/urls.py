from django.conf.urls import url

from .views import reminders

urlpatterns = [
    url('^reminders/', reminders),
]
