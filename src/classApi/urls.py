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
from forum.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('timesc/<str:pk>/<str:ymd>/', getData),
    path('food/<int:pk>/<str:ymd>/', getDatalunc), 
    path('signup/<str:stclasstype>/<str:school>/<str:edumintype>/<int:grade>', signUpUser),
    path('signup/<str:stclasstype>/<str:school>/<str:edumintype>/<int:grade>/<str:user>/<str:pw>', signUpUserGet),
    path('logcheck/', logcheck),
    path('logcheckGet/<str:user>/<str:password>', logcheckGet),
    path('todoList/view/<int:pk>/',todoGet),
    path('todoList/create/<int:pk>/<str:title>/<str:body>/<str:subject>',todoCreate),
  path('getlocals/', getLocalGroups),
  path('getgalaxies/<str:state>', getGalax),
  path('getschool/<str:state>/<str:local>/<str:schltype>', getSys),
  path('forum/send/<int:forumPk>/<int:studentPk>', writePost),
  path('forum/sendGet/<int:forumPk>/<int:studentPk>/<str:title>/<str:body>', writePostGet),
  path('forum/query/<int:forumPk>/', getPosts ),
  path('forum/like/<int:postid>', like),
  path('testLinkkor', 씨발_어쩌다가_내인생이_이지랄이_됐는지는_모르겠지만_하_개피곤하네_씨이이이이바아알)
  
  
    
]
