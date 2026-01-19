from django.shortcuts import render,redirect 
from .forms import RegisterForm , LoginForm
from django.contrib import messages 
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

def accueil(request):
    return render (request , "Accueil.html")

def pageutilisateur(request):
    return render(request,"page_utilisateur.html")

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

from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import LoginForm

def login_view(request):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        user = form.cleaned_data["user"]
        login(request, user)
        return redirect("page_utilisateur")
    return render(request, "login.html", {"form": form})


@login_required(login_url='/login/')
def page_protegee(request):
    return render(request,'Accueil.html')  