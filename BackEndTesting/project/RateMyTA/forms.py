import email
from django import forms 

class SignupForm(forms.Form): 
    #name = forms.CharField(label = 'Your Name', max_length = 100)
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))
class LoginForm(forms.Form):
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))

class SearchForm(forms.Form):
    searchQuery = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control w-50 mx-auto', 'id': 'searchBar'}))

class NewReviewForm(forms.Form):
    courseCode = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea'}))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea'}))
    body = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea2', 'style': 'height: 100px'}))
    rating = forms.IntegerField(required=True, widget=forms.NumberInput(attrs={'class': 'form-select', 'id': 'floatingSelect'}))