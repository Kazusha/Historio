from django.urls import path
from .views import accueil , register_view ,login_view , pageutilisateur , mes_livres ,ajouterLivre,detail_livre,likes,saves,supprimerLivre

urlpatterns = [
    path("", accueil, name="accueil"),
    path('inscription/', register_view , name='inscription'),
    path('login/',login_view, name='login'),
    path('page_utilisateur/', pageutilisateur ,name ='page_utilisateur'),
    path("mes-livres/", mes_livres, name="mes_livres"),
    path("ajouterLivre",ajouterLivre,name="ajouterLivre"),
    path('livre/<int:id>/' , detail_livre , name='detail_livre'),
    path('livre/<int:id>/likes',likes,name='likes'),
    path('livre/<int:id>/saves/',saves,name='saves'),
    path('livre/<int:id>/supprimer/',supprimerLivre,name="supprimerLivre"),

]
