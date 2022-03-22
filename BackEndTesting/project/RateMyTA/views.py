import email
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import SearchForm, SignupForm
from .forms import LoginForm
from .models import addUser, searchForTA
from .models import verifyUser



# Create your views here.
def showSignup(request):
    submitbutton= request.POST.get("submit")

    full_name=''
    email=''
    password=''
   
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            full_name = form.cleaned_data.get("name")
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            addUser(full_name,email,password)
    else:
        form = SignupForm()
    context = {'form': form, 'full_name':full_name,'email':email,'password':password,'submitbutton':submitbutton}
    return render( request, 'signup.html', context)




# def showStartPg(request):
#     return render(request, 'startpg.html')

def showSearch(request):

    searchButton = request.GET.get("submit")

    searchString = ''

    if request.method == 'GET':

        form = SearchForm(request.GET)
        if form.is_valid():

            print("ahhhhhhhh")
            searchString = form.cleaned_data.get("searchQuery")
            searchForTA(searchString)
    else:
        form = SearchForm()

    context = {'form': form,'searchString': searchString, 'searchButton':searchButton}
    return render(request, 'search.html', context)




def showLogin(request):
    submitbutton= request.POST.get("submit")

    full_name=''
    email=''
    password=''
    # connect to db
    # pass to html page
    # return render(request, 'main.html')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            verifyUser(email,password)
    else:
        form = LoginForm()
    context = {'form': form,'email':email,'password':password,'submitbutton':submitbutton}
    return render( request, 'login.html', context)

def showNewReview(request):
    return render(request, 'newReview.html')