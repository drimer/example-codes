from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from people.dependency_injection.container import DIContainer

router = DefaultRouter()
router.register(r'person', DIContainer.person_view_set())

urlpatterns = (
    url(r'^', include(router.urls)),
)
