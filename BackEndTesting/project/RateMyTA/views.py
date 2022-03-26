import email
from re import search
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .forms import SearchForm, SignupForm, TaRequestForm
from .forms import LoginForm, NewReviewForm
from .models import addUser, searchForTA
from .models import verifyUser, createReview, findReviews, findTAByID
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail



# 
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
            if(User.objects.filter(username=full_name).exists()):
                messages.error(request, "Username already exists. Please try again.")
                return redirect('signup')                 
            else:
                newUser = User.objects.create_user(full_name,email,password)
                messages.success(request, 'Sign up successful')
                return redirect('../login')

    else:
        form = SignupForm()
    context = {'form': form, 'full_name':full_name,'email':email,'password':password,'submitbutton':submitbutton}
    return render( request, 'signup.html', context)



# shows the search page
def showSearch(request):

    searchButton = request.POST.get("submit")

    searchString = ''

    if request.method == 'POST':

        form = SearchForm(request.POST)
        if form.is_valid():
            searchString = form.cleaned_data.get("searchQuery")
            # searchForTA(searchString)
            return redirect('search-results', ss=searchString)

    else:
        form = SearchForm()

    context = {'form': form,'searchString': searchString, 'searchButton':searchButton}
    return render(request, 'search.html', context)



def showSearchResults(request, ss):

    data = searchForTA(ss)
    for item in data:
        item['id'] = str(item['_id'])
    
    if data != None:
        context = {'data': data,"searchString": ss, 'results':True}
    else:
        context = {'data': data,"searchString": ss, 'results':False}
    return render(request,'search-results.html', context)



def showReviewResults(request):
    taId = request.POST.get('submitButton', None)
    reviews = findReviews(taId)
    orderedReviews = reversed(reviews)
    TA = findTAByID(taId)
    if reviews != None:
        context = {'reviews': orderedReviews, 'size':len(reviews), 'TA': TA, 'id':TA['_id']}
    else:
        context = {'reviews': orderedReviews, 'size':len(reviews), 'TA': TA}
    return render(request, 'review-results.html', context)    
  


def showLogin(request):
    logout(request)
    submitbutton= request.POST.get("submit")

    full_name=''
    email=''
    password=''
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request, user)
                messages.success(request, 'You are logged in!')
                return redirect('../')
            else:
                messages.error(request, "Invalid login information. Please try again.")
                return redirect('login')

    else:
        form = LoginForm()
    context = {'form': form,'email':email,'password':password,'submitbutton':submitbutton}
    return render( request, 'login.html', context)


def showNewReview(request):
    if request.user.is_authenticated:
        taId = request.POST.get('startReviewButton', None)
        TA = findTAByID(taId)
        submitbutton= request.POST.get("submit")
        
        taIdentifier = taId
        body=''
        courseCode=''
        rating=''
        title = ''

        if request.method == 'POST':
            form = NewReviewForm(request.POST)          

            if form.is_valid():
                title = form.cleaned_data.get("title")
                body = form.cleaned_data.get("body")
                courseCode = form.cleaned_data.get("courseCode")
                rating = form.cleaned_data.get("rating")
                taIdentifier = form.cleaned_data.get("taID")
                createReview(title, body, courseCode, rating, taIdentifier)
                messages.success(request, 'Review was created successfully!')
                return redirect('../')

        else:
            form = NewReviewForm()

        if TA != None:
            context = {'form': form, 'title':title,'body':body,'courseCode':courseCode,'rating':rating, 'submitbutton': submitbutton, 'TA': TA, 'id':TA['_id']}
        else:
            context = {'form': form, 'title':title,'body':body,'courseCode':courseCode,'rating':rating, 'submitbutton': submitbutton, 'TA': TA}
        return render( request, 'new-review.html', context)
       
    else:
        return redirect('../login')



def showTARequest(request): 
    submitbutton = request.POST.get("submit")

    name = ''
    school = ''

    if request.method == 'POST':
        form = TaRequestForm(request.POST)
            
        if form.is_valid():
            name = form.cleaned_data.get("name")
            school = form.cleaned_data.get("school")
            msg = 'TA Name:' + name + ' School:' + school
            subject = 'New TA Request'

            send_mail(subject = subject, message=msg,from_email=settings.EMAIL_HOST_USER,recipient_list =[settings.RECIPIENT_ADDRESS])
            return redirect('../')

            
    else:
        form = TaRequestForm()
    context = {'form':form, 'submitbutton':submitbutton}
    return render(request, 'ta-request.html', context)