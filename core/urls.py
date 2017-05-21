from django.conf.urls import url
from core.views import home, luz, ventilador, tradutor

urlpatterns = [
    url(r'^$', home, name='home'),
    url(r'^luz$', luz, name='luz'),
    url(r'^ventilador$', ventilador, name='ventilador'),
    url(r'^tradutor$', tradutor, name='tradutor'),
]
