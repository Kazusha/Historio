from django import forms 
from django.contrib.auth.forms import UserCreationForm
from .models import Livre , Chapitre
from django.contrib.auth import get_user_model
from ckeditor.widgets import CKEditorWidget
from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Adresse email")
    photo_user  = forms.ImageField(required=False, label="Photo de profil (optionnel)")
    
    class Meta:
        model = User
        fields = ("username", "email", "photo_user", "password1", "password2")
        labels = {
            "username": "Pseudo",
            "password1": "Mot de passe",
            "password2": "Confirmer le mot de passe",
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({"placeholder": "Votre pseudo"})
        self.fields['email'].widget.attrs.update({"placeholder": "votremail@example.com"})
        self.fields['password1'].widget.attrs.update({"placeholder": "••••••••"})
        self.fields['password2'].widget.attrs.update({"placeholder": "••••••••"})
        self.fields['password1'].help_text = "Au minimum 8 caractères"

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Les mots de passe ne correspondent pas")
        return password2
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Cet email est déjà utilisé")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]  
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({"placeholder": "votremail@example.com"})
        self.fields['password'].widget.attrs.update({"placeholder": "••••••••"})

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Email ou mot de passe incorrect")

            user = authenticate(username=user_obj.username, password=password)
            if not user:
                raise forms.ValidationError("Email ou mot de passe incorrect")

            cleaned_data["user"] = user 
        return cleaned_data
    
class AjouterLivre(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre' , 'couverture' , 'description']
        labels = {
            'titre': 'Titre de l\'histoire',
            'couverture': 'Couverture',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 6,
                'class': 'textarea-field',
                'placeholder': 'Décrivez votre histoire...'
            }),
            'titre': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Titre de votre histoire'
            }),
        }

class AjouterChapitre(forms.ModelForm):
    contenu = forms.CharField(widget=CKEditorWidget, label="Contenu")
    class Meta:
        model = Chapitre
        fields=['numero_chap','titre_chap','contenu']
        labels = {
            'numero_chap': 'Numéro du chapitre',
            'titre_chap': 'Titre du chapitre',
        }

class ModifierLivre(forms.ModelForm):
    class Meta:
        model = Livre
        fields = ['titre' , 'couverture' , 'description']
        labels = {
            'titre': 'Titre de l\'histoire',
            'couverture': 'Couverture',
            'description': 'Description',
        }
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 6,
                'class': 'textarea-field',
                'placeholder': 'Décrivez votre histoire...'
            }),
            'titre': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Titre de votre histoire'
            }),
        }

  