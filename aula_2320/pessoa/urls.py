from django.urls import path
from . import views

app_name = 'pessoa' 

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:id_pessoa>/', views.detalhe, name='detalhe'),
    path('read/', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('update/<int:id_pessoa>/', views.update, name='update'),
    path('delete/<int:id_pessoa>/', views.delete, name='delete'),
]
