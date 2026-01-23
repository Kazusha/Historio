from django.urls import path
from .views import accueil , register_view ,login_view , pageutilisateur , mes_livres ,ajouterLivre

urlpatterns = [
    path("", accueil, name="accueil"),
    path('inscription/', register_view , name='inscription'),
    path('login/',login_view, name='login'),
    path('page_utilisateur/', pageutilisateur ,name ='page_utilisateur'),
    path("mes-livres/", mes_livres, name="mes_livres"),
    path("ajouterLivre",ajouterLivre,name="ajouterLivre"),
]
