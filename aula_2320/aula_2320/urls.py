from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView 
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('conta/', include('django.contrib.auth.urls')),
    path('pessoa/', include('pessoa.urls')),
    path('setor/', include('setor.urls')),
    path('filial/', include('filial.urls')),
]
