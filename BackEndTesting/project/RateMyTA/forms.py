import email
from django import forms 

class SignupForm(forms.Form): 
    name = forms.CharField(label = 'Your Name', max_length = 100)
    email = forms.CharField(label = 'Email', max_length = 100)
    password = forms.CharField(label = 'Password', max_length = 100)
