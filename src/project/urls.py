"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from RateMyTA import views

urlpatterns = [
    path('', views.showSearch, name='search'),
    path('admin/', admin.site.urls),
    path('login/', views.showLogin, name='login'),
    path('signup/', views.showSignup, name='signup'),
    path('search-results/<str:ss>/', views.showSearchResults, name='search-results'),
    path('new-review/', views.showNewReview, name='new-review'),
    path('review-results/', views.showReviewResults, name='review-results'),
    path('ta-request/', views.showTARequest, name = 'ta-request'),
]
