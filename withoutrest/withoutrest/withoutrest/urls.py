"""withoutrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from withoutrestapp import views
from django.conf.urls import url
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', views.emp_data_view),
    #url(r'api/', views.emp_data_view ),
     path('apijson/', views.emp_data_jsonview),
    #url(r'apijson/', views.emp_data_jsonview ),
     path('apijson2/', views.emp_data_jsonview2),
    #url(r'apijson2/', views.emp_data_jsonview2),
    path('apijsoncbv/', views.JsonCBV.as_view()),
    #url(r'apijsoncbv/', views.JsonCBV.as_view()), 
    # path('apijsoncbv2/', views.JsonCBVwithoutioDict.as_view()),
]
