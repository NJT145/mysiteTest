from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^entries/$', show_blog),
    url(r'^entries/(?P<entry_id>[0-9]+)', get_blog_entry),
    url(r'^entries/all$', show_all_blog),
    url(r'^entries/all/user/(?P<userId>[0-9]+)$', show_all_blog_from_user),
]
