from django.shortcuts import render,redirect 
from .forms import RegisterForm
from django.contrib import messages 

# Create your views here.
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