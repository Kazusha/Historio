from django.urls import path
from .views import accueil , register_view ,login_view , mes_livres ,ajouterLivre,detail_livre,likes,saves,supprimerLivre, home, ajouterchap_view, modifier_livre , bibliotheque

urlpatterns = [
    path("", accueil, name="accueil"),
    path('inscription/', register_view , name='inscription'),
    path('login/',login_view, name='login'),
    path("mes-livres/", mes_livres, name="mes_livres"),
    path("ajouterLivre",ajouterLivre,name="ajouterLivre"),
    path('livre/<int:id>/' , detail_livre , name='detail_livre'),
    path('livre/<int:id>/likes',likes,name='likes'),
    path('livre/<int:id>/saves/',saves,name='saves'),
    path('livre/<int:id>/supprimer/',supprimerLivre,name="supprimerLivre"),
    path('livre/<int:id>/modifier/', modifier_livre, name='modifier_livre'),
    path("home",home,name='home'),
    path('livre/<int:livre_id>/ajouter-chapitre/', ajouterchap_view, name='ajouter_chapitre'),
    path('livre/<int:livre_id>/chapitres/', ajouterchap_view, name='livre_view_parlivre'),  
    path('bibliotheque/',bibliotheque , name='bibliotheque')
]
