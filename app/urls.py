# -*- coding: utf-8 -*-
from django.urls import path
from . import views

urlpatterns = [
        path('',views.home,name='home'),
        path('login',views.login,name='login'),
        path('signup',views.signup,name='signup'),
        path('slogin',views.slogin,name='slogin'),
        path('ssignup',views.ssignup,name='ssignup'),
        path('predict',views.predict,name="predict"),
        path('consult',views.consult,name="consult")
        ]
