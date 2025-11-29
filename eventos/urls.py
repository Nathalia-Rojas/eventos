from django.urls import path
from . import views

urlpatterns = [
    path('', views.EventoListView.as_view(), name='evento_list'),
    path('evento/<int:pk>/', views.EventoDetailView.as_view(), name='evento_detail'),
    path('evento/crear/', views.EventoCreateView.as_view(), name='evento_create'),
    path('evento/<int:pk>/editar/', views.EventoUpdateView.as_view(), name='evento_update'),
    path('evento/<int:pk>/eliminar/', views.EventoDeleteView.as_view(), name='evento_delete'),
    
    # Tarea: Redirección de Accesos No Autorizados
    path('acceso-denegado/', views.AccesoDenegadoView.as_view(), name='acceso_denegado'),
]