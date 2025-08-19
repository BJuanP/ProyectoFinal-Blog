from .forms import RegistroUsuarioForm
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import CreateView
from django.contrib import messages
from django.shortcuts import redirect
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.models import Group

from .models import Usuario

# Create your views here.

class registrarUsuario(CreateView):
    template_name = 'registration/registrar.html'
    form_class = RegistroUsuarioForm
    
    def form_valid(self,form):
        messages.success(self.request, 'Registro Exitoso. Por favor, inicia sesion')
        usuario = form.save()
        grupo_miembro, _ = Group.objects.get_or_create(name='Miembro')
        usuario.groups.add(grupo_miembro) 
        
        return redirect('apps.usuario:login')

class LoginUsuario(LoginView):
    template_name = 'registration/login.html'
    
    def get_success_url(self):
        messages.success(self.request, 'Login Exitoso')
        
###class LogoutUsuario(LogoutView):
#    template_name = 'registration/logout.html'
#    
#    def get_success_url(self):
#        messages.success(self.request, 'Logout Exitoso')
#        
#        return reverse('apps.usuario:logout')

class LogoutUsuario(LogoutView):
    next_page = reverse_lazy('path_home')  

    def dispatch(self, request, *args, **kwargs):
        messages.success(self.request, 'Logout exitoso')
        return super().dispatch(request, *args, **kwargs)
    

class PerfilUsuario(LoginRequiredMixin, DetailView):
    model = Usuario
    template_name = 'usuarios/perfil.html'
    context_object_name = 'usuario'

    def get_object(self):
        return self.request.user


class EditarPerfil(LoginRequiredMixin, UpdateView):
    model = Usuario
    template_name = 'usuarios/editar_perfil.html'
    fields = ['first_name', 'last_name', 'email']  # Campos editables
    success_url = reverse_lazy('usuario:perfil') 

    def get_object(self):
        return self.request.user

@login_required
def perfil(request):
    return render(request, 'usuarios/perfil.html', {'usuario': request.user})

@login_required
def editar_perfil(request):
    return render(request, 'usuarios/editar_perfil.html', {'usuario': request.user})
