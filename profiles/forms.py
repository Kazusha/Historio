from django import forms 
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth import get_user_model

User = get_user_model()
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo_user  = forms.ImageField(required=False)


    class Meta:
        model = User
        fields = ("username","email","photo_user","password1","password2")

class LoginForm(AuthenticationForm):
    pass