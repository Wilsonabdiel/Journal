
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry", views.entry, name="entry"),
    path('delete/<int:id>', views.delete, name="delete"),
]
