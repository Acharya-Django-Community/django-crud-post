from django.urls import path
from .views import *

urlpatterns = [
    path('', post_list,name='post_list'),
    path('posts/<slug:slug>/', post_detail,name='post_detail'),
    path('create/', post_create,name='post_create'),

]