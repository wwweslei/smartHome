from django.conf.urls import url
from core.views import home, luz, ventilador
urlpatterns = [
    url(r"^$",  name="home"),
    url(r"^luz$", luz, name="luz"),
    url(r"^ventilador$", ventilador, name="ventilador"),
]
