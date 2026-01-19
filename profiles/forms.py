from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django import forms
from django.contrib.auth import authenticate, get_user_model

User = get_user_model()
 
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    photo_user  = forms.ImageField(required=False)

    class Meta:
        model = User
        fields = ("username", "email", "photo_user", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]  # ✅ corrige ici
        if commit:
            user.save()
        return user

class LoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        password = cleaned_data.get("password")

        if email and password:
            try:
                user_obj = User.objects.get(email=email)
            except User.DoesNotExist:
                raise forms.ValidationError("Email ou mot de passe invalide")

            user = authenticate(username=user_obj.username, password=password)
            if not user:
                raise forms.ValidationError("Email ou mot de passe invalide")

            cleaned_data["user"] = user 
        return cleaned_data