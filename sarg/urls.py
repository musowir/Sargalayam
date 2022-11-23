
from django.urls import re_path as url
from sarg import views
from django.urls import path
# SET THE NAMESPACE!
app_name = 'sarg'
# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[

    path("catsel", views.catsel, name="catsel"),
    path("result", views.result, name="result"),

]