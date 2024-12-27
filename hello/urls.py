from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("jaweria", views.jaweria, name="jaweria"),
    path("<str:name>", views.greet, name="greet")
]