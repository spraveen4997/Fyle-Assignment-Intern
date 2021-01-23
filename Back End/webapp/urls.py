# myapi/urls.py
from django.urls import include, path,re_path
from .import views 
urlpatterns = [
    re_path(r'^branches/(?P<ac>\w+|$)$', views.BankAPI.as_view()),
]