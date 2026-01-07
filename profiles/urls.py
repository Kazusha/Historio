from django.urls import path
from .views import accueil , register_view ,login_view

urlpatterns = [
    path("", accueil, name="accueil"),
    path('inscription/', register_view , name='inscription'),
    path('login/',login_view, name='login'),
]
