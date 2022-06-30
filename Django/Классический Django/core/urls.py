from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("news/", views.news, name="news"),
    path("personal_areal/", views.personal_areal, name="personal_areal"),
    path("tarif/", views.tarif, name="tarif"),
    path("test/", views.test, name="test"),
]
