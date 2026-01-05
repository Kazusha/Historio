from django.urls import path
from .views import accueil , register_view

urlpatterns = [
    path("", accueil, name="accueil"),
    path('inscription/', register_view , name='inscription'),
]
