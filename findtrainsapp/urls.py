from django.urls import path
from findtrainsapp.views import *

urlpatterns = [
    path('',findtrains,name='find'),
]
