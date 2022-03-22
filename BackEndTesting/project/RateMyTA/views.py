import email
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import SearchForm, SignupForm
from .forms import LoginForm, NewReviewForm
from .models import addUser, searchForTA
from .models import verifyUser, createReview



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

    searchButton = request.POST.get("submit")

    searchString = ''

    if request.method == 'POST':

        form = SearchForm(request.POST)
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
    submitbutton= request.POST.get("submit")

    body=''
    courseCode=''
    rating=''
    title = ''

    print(request.method)

    if request.method == 'POST':
        form = NewReviewForm(request.POST)

        if form.is_valid():
            title = form.cleaned_data.get("title")
            body = form.cleaned_data.get("body")
            courseCode = form.cleaned_data.get("courseCode")
            rating = form.cleaned_data.get("rating")
            createReview(title, body, courseCode, rating)
        else:
            print(form.errors)

    else:
        form = NewReviewForm()
  
    context = {'form': form, 'title':title,'body':body,'courseCode':courseCode,'rating':rating, 'submitbutton': submitbutton}
    return render( request, 'newReview.html', context)

def showSearchResults(request):
    return render( request, 'search-results.html')