from django.shortcuts import render,redirect 
from .forms import RegisterForm , LoginForm , AjouterChapitre , AjouterLivre
from django.contrib import messages 
from django.contrib.auth import login
from .models import Livre
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.shortcuts import get_object_or_404

def accueil(request):
    return render (request , "Accueil.html")

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST , request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request , "Votre compte a ete creer Vous pouvez maintenant vous connecter")
            return redirect ('login')
    else:
         form = RegisterForm()
    return render(request , 'register.html', {'form' : form})   



def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = form.cleaned_data["user"]
        login(request, user)
        return redirect("page_utilisateur")
    return render(request, "login.html", {"form": form})

@login_required(login_url="/login/")
def pageutilisateur(request):
    return render(request, "page_utilisateur.html")

@login_required(login_url="/login/")
def mes_livres(request):
    livres = Livre.objects.filter(user=request.user)
    return render(request , "mes_livres.html")

@login_required(login_url="/login/")
def ajouterLivre_view(request):
    if request.method == "POST":
         form = AjouterLivre(request.POST, request.FILES)
         if form.is_valid():
           form.save()
           return redirect("livre_view")
    else:
         form =AjouterLivre()
    return render(request,"livre_view.html",{"form":form})

@login_required(login_url="/login/")
def ajouterchap_view(request , livre_id):
    livre = get_object_or_404(livre , pk=livre_id)
    if request.method == "POST":
     form = AjouterChapitre(request.POST)
     if form.is_valid():
        chapitre = form.save(commit=False)
        chapitre.livre = livre
        chapitre.save()
        return redirect("livre_view_parlivre",livre_id=livre.id)
    else:
        form=AjouterChapitre() 
    return render(request , "livre_view_parlivre.html" , {"form":form , "livre":livre})


@login_required(login_url='/login/')
def page_protegee(request):
    return render(request,'Accueil.html')  