from django.urls import path
from . import views
from .views import LoginUsuario
from django.contrib.auth import views as auth_views
from .views import PerfilUsuario, EditarPerfil

app_name = 'apps.usuario'

urlpatterns = [
    path('registrar/', views.registrarUsuario.as_view(), name='registrar'),
    #path('login/', LoginUsuario.as_view(), name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', views.LogoutUsuario.as_view(), name='logout'),
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('perfil/', PerfilUsuario.as_view(), name='perfil'),
    path('perfil/editar/', EditarPerfil.as_view(), name='editar_perfil'),
    path('perfil/cambiar-password/', auth_views.PasswordChangeView.as_view(template_name='usuarios/cambiar_password.html', success_url='/usuario/perfil/'), name='cambiar_password'),
    
]