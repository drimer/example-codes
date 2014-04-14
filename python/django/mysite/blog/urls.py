from django.conf.urls import patterns

from blog.views import archive


urlpatterns = patterns('blog.views',
    (r'^$', archive),
)
