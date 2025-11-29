from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Django nos da un conjunto de URLs ya hechas para login, logout, cambio de contraseña, etc.
    # Esto manejará automáticamente /login, /logout, etc.
    path('accounts/', include('django.contrib.auth.urls')),
    
    # Incluimos las URLs de nuestra aplicación de eventos
    path('', include('eventos.urls')),
]