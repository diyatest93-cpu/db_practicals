from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show/', views.show, name='show'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.update, name='edit'),
    path('search/', views.search, name='search'),
    path('login', views.login, name='login'),
    
    
]
