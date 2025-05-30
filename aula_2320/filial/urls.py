from django.urls import path
from . import views

app_name = 'filial'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:id_filial>/', views.detalhe, name='detalhe'),
    path('read/', views.read, name='read'),
    path('create/', views.create, name='create'),
    path('update/<int:id_filial>/', views.update, name='update'),
    path('delete/<int:id_filial>/', views.delete, name='delete'),
]
