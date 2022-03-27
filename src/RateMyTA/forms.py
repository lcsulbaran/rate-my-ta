import email
from django import forms 
from django.core.exceptions import ValidationError

# form fields for the new user signup page
class SignupForm(forms.Form): 
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    email = forms.CharField(required=True, widget=forms.EmailInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))
    
# form fields for the user login page
class LoginForm(forms.Form):
    username = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'class': 'form-control', 'id': 'floatingPassword'}))

# form fields for the search page
class SearchForm(forms.Form):
    searchQuery = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))

# form fields for the new review page
class NewReviewForm(forms.Form):
    courseCode = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea'}))
    title = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea'}))
    body = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingTextArea2', 'style': 'height: 100px'}))
    rating = forms.IntegerField(required=True, min_value = 0, max_value = 10, widget=forms.NumberInput(attrs={'class': 'form-select', 'id': 'floatingSelect'}))
    taID = forms.CharField(widget=forms.HiddenInput(), required=False)

# form fields for the new TA request page
class TaRequestForm(forms.Form): 
    name = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
    school = forms.CharField(required = True, widget=forms.TextInput(attrs={'class': 'form-control', 'id': 'floatingInput'}))
