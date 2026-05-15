from django.urls import path
from . import views

urlpatterns = [ path('api/v1/short-codes' , views.shorten_url, name='shorten_url'),
               path('api/v1/short-codes/<str:short_code>',views.redirect_url, name='redirect_url')]