from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^', views.index),
    url(r'^shop/checkout$', views.checkout),
    url(r'^shop/success$', views.success)
]