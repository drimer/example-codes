from django.conf.urls import patterns


urlpatterns = patterns('blog.views',
    (r'^$', 'archive'),
)
