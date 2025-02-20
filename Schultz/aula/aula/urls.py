"""
URL configuration for aula project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from pessoa import views as view_pessoa

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa/', view_pessoa.Index, name='index-pessoa'),
    path('pessoa/listar/', view_pessoa.ler, name='ler-pessoa'),
    path('pessoa/<int:idPessoa>/', view_pessoa.detalhar, name='detalhar-pessoa'), 
    path('pessoa/atualizar/', view_pessoa.atualizar, name='atualizar-pessoa'),
    path('pessoa/deletar/', view_pessoa.deletar, name='deletar-pessoa')
]
