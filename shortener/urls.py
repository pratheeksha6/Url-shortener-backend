from django.urls import path
from . import views

urlpatterns = [ path('api/v1/short-codes' , views.shorten_url, name='shorten_url')]