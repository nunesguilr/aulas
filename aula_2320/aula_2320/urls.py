from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/logout/', auth_views.LogoutView.as_view(template_name='registration/logged_out.html'), name='logout'),
    path('conta/', include('django.contrib.auth.urls')),
    path('pessoa/', include('pessoa.urls', namespace='pessoa')), 
    path('setor/', include('setor.urls', namespace='setor')),   
    path('filial/', include('filial.urls', namespace='filial')), 
]
