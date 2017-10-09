from django.conf.urls import url
from rest_framework.authtoken.views import obtain_auth_token

from webapp.views import RemindersView

urlpatterns = [
    url('^reminders/', RemindersView.as_view()),
    url('^auth/login/', obtain_auth_token, name='login'),
]
