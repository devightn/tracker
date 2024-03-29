"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include, re_path
from tracker import views
from tracker.views import EventView, EventDetailView


urlpatterns = [
     path('', views.index, name='index'),
     path('<int:event_id>/', views.detail, name='detail'),
     path('api/v1/events/', EventView.as_view()),
     re_path('api/v1/event/(?P<event_id>.*)', EventDetailView.as_view())
]
