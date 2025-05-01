from django.urls import path

from .views import index, image_get, clock_get


urlpatterns = [
    path("", index),
    path("get/", image_get),
    path("clock/", clock_get),
]