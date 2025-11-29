from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib import messages
from django.core.exceptions import PermissionDenied

from .models import Evento

# Vista para la página de "Acceso Denegado"
class AccesoDenegadoView(TemplateView):
    template_name = 'acceso_denegado.html'

# Mixin personalizado para manejar mensajes de error de permisos
class CustomPermissionMixin(PermissionRequiredMixin):
    def handle_no_permission(self):
        messages.error(self.request, "No tienes permiso para realizar esta acción.")
        # Tarea: Redirección de Accesos No Autorizados
        return redirect('acceso_denegado')

# Vista para listar todos los eventos (pública)
class EventoListView(ListView):
    model = Evento
    template_name = 'evento_list.html'
    context_object_name = 'eventos'

# Vista para ver el detalle de un evento (pública)
class EventoDetailView(DetailView):
    model = Evento
    template_name = 'evento_detail.html'

# Vista para crear un evento
# Tarea: Uso de Mixins en el Modelo Auth
class EventoCreateView(LoginRequiredMixin, CustomPermissionMixin, CreateView):
    model = Evento
    fields = ['nombre', 'fecha', 'ubicacion']
    template_name = 'evento_form.html'
    permission_required = 'eventos.add_evento' # Permiso para "añadir evento"

    def form_valid(self, form):
        form.instance.organizador = self.request.user
        messages.success(self.request, "¡Evento creado con éxito!")
        return super().form_valid(form)

# Vista para editar un evento
class EventoUpdateView(LoginRequiredMixin, CustomPermissionMixin, UpdateView):
    model = Evento
    fields = ['nombre', 'fecha', 'ubicacion', 'asistentes']
    template_name = 'evento_form.html'
    permission_required = 'eventos.change_evento' # Permiso para "cambiar evento"
    
    def form_valid(self, form):
        messages.success(self.request, "¡Evento actualizado con éxito!")
        return super().form_valid(form)


# Vista para eliminar un evento
class EventoDeleteView(LoginRequiredMixin, CustomPermissionMixin, DeleteView):
    model = Evento
    template_name = 'evento_confirm_delete.html'
    success_url = reverse_lazy('evento_list')
    permission_required = 'eventos.delete_evento' # Permiso para "eliminar evento"

    def form_valid(self, form):
        messages.success(self.request, "Evento eliminado correctamente.")
        return super().form_valid(form)