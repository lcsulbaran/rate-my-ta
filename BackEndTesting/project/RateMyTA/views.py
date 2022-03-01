from urllib import request
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showPage(request):
    # connect to db
    # pass to html page
    return render(request, 'main.html')

def showNextPage(request):
    return render(request, 'done.html')
