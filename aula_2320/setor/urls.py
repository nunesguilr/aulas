from django.urls import path
from . import views

app_name = 'setor' 

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:id_setor>/', views.detalhe, name='detalhe'),
    path('read/', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('update/<int:id_setor>/', views.update, name='update'),
    path('delete/<int:id_setor>/', views.delete, name='delete'),
]
