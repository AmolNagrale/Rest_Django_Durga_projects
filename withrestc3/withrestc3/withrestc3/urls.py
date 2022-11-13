"""withrestc3 URL Configuration

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
from testapp import views
from django.conf.urls import include
from django.urls import re_path as url

urlpatterns = [

    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', views.EmployeeListAPIView.as_view()),
    # path('api/', views.EmployeeCreateAPIView.as_view()),
    # path('api/', views.EmployeeRetrieveAPIView.as_view()),
    # url(r'^api/',views.EmployeeCreateAPIView.as_view()),
    # url(r'^api/(?P<pk>\d+)/$',views.EmployeeRetrieveAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$',views.EmployeeUpdateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$',views.EmployeeDestroyAPIView.as_view()),
    # path('api/', views.EmployeeListCreateAPIView.as_view()),
    # url(r'^api/$',views.EmployeeListCreateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveUpdateAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveDestroyAPIView.as_view()),
    # url(r'^api/(?P<id>\d+)/$',views.EmployeeRetrieveUpdateDestroyAPIView.as_view()),
    # path('api/', views.EmployeeListCreateModelMixin.as_view()),
    # url(r'^api/(?P<pk>\d+)/$',views.EmployeeRetrieveUpdateDestroyModelMixin.as_view())
] 
