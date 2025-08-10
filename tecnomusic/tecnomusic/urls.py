"""
URL configuration for tecnomusic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin # Importa la clase admin para el panel de administración
from django.urls import path,include # Importa las funciones path e include para definir rutas
from productos.views import inicio # Importa la vista de inicio desde el módulo productos.views

urlpatterns = [
   path('admin/', admin.site.urls), # ruta para el panel de administración
   path('', inicio, name='inicio'), #ruta para la página de inicio
   path('productos/', include('productos.urls')),  # ruta para las vistas de productos
]