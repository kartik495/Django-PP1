
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('sign',views.sign,name='sign'),
    path('add',views.add,name='add'),
    path('delete',views.delete,name='delete'),
    path('show',views.show,name='show')
]
