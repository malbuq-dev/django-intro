from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:name>", views.readPage, name="readPage"),
    path("createNewPage/", views.createNewPage, name="createNewPage"),
    path("randomPage/", views.randomPage, name="randomPage"),
    path("editPage/<str:title>", views.editPage, name="editPage"),
]
