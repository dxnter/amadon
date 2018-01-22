from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^shop/', views.index),
    url(r'^checkout$', views.checkout),
    url(r'^success$', views.success)
]