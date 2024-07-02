from django import forms

class LoginForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput)
    email = forms.EmailField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    nombre = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    telefono = forms.IntegerField()
    email = forms.EmailField()