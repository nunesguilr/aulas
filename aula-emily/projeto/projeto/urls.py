"""
URL configuration for projeto project.

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
from pessoa import views as pessoa_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pessoa/', pessoa_view.main, name='main-pessoa'),
    path('pessoa/<int:id_pessoa>/', pessoa_view.detalhe, name='detalhe-pessoa'), 
    path('pessoa/read/', pessoa_view.read, name='read-pessoa'),
    path('pessoa/create/', pessoa_view.create, name='create-pessoa'),
    path('pessoa/update/', pessoa_view.update, name='update-pessoa'),
    path('pessoa/delete/', pessoa_view.delete, name='delete-pessoa'),
]