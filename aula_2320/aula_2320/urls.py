from django.contrib import admin
from django.urls import path, include
from pessoa import views as vw_pessoa
from setor import views as vw_setor
from filial import views as vw_filial 

urlpatterns = [
    path('admin/', admin.site.urls),

    path('pessoa/', vw_pessoa.main, name='main-pessoa'),
    path('pessoa/<int:id_pessoa>/', vw_pessoa.detalhe, name='detalhe-pessoa'),
    path('pessoa/read/', vw_pessoa.read, name='read-pessoa'),
    path('pessoa/create/', vw_pessoa.create, name='create-pessoa'),
    path('pessoa/update/<int:id_pessoa>/', vw_pessoa.update, name='update-pessoa'),
    path('pessoa/delete/<int:id_pessoa>/', vw_pessoa.delete, name='delete-pessoa'),

    path('setor/', vw_setor.main, name='main-setor'),
    path('setor/<int:id_setor>/', vw_setor.detalhe, name='detalhe-setor'),
    path('setor/read/', vw_setor.read, name='read-setor'),
    path('setor/create/', vw_setor.create, name='create-setor'),
    path('setor/update/<int:id_setor>/', vw_setor.update, name='update-setor'),
    path('setor/delete/<int:id_setor>/', vw_setor.delete, name='delete-setor'),

    path('filial/', vw_filial.main, name='main-filial'),
    path('filial/<int:id_filial>/', vw_filial.detalhe, name='detalhe-filial'),
    path('filial/read/', vw_filial.read, name='read-filial'),
    path('filial/create/', vw_filial.create, name='create-filial'),
    path('filial/update/<int:id_filial>/', vw_filial.update, name='update-filial'),
    path('filial/delete/<int:id_filial>/', vw_filial.delete, name='delete-filial'),
]
