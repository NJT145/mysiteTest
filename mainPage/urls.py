from django.conf.urls import url

from .views import overview

urlpatterns = [
    url(r'^$', overview),
]
