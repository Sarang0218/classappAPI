"""classApi URL Configuration

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
from api.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/timesc/<int:year>/<str:ymd>/<str:sem>/', getData),
    path('api/food/<str:sc>/<str:ymd>/', getDatalunc), 
    path('api/signup/<str:stclasstype>/<str:edumintype>/<int:grade>', signUpUser),
    path('api/logcheck/', logcheck),
    path('api/todoList/view/<int:pk>/',todoGet),
    path('api/todoList/create/<int:pk>/<str:title>/<str:body>/<str:subject>',todoCreate),
  
  
]
