import email
from django import forms 

class SignupForm(forms.Form): 
    #name = forms.CharField(label = 'Your Name', max_length = 100)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))

class LoginForm(forms.Form):
    email = forms.CharField(label = 'Email', max_length = 100)
    password = forms.CharField(label = 'Password', max_length = 100)