from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^adprofile', views.adprofile, name='adprofile'),
#    url(r'^$', views.index, name='index'),
]
