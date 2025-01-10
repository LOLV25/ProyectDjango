"""
URL configuration for whatsapp project.

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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from core.views import UsuarioViewSet, EstadoViewSet
from core import views  # Importa las vistas de la app 'core'

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet)
router.register(r'estados', EstadoViewSet)

# Define las rutas de la app 'whatsapp'
urlpatterns = [
    path('admin/', admin.site.urls),  # Ruta para el admin
    path('api/', include(router.urls)),  # Ruta para la API
    # Aquí puedes agregar más rutas relacionadas a la app 'core' o las vistas propias de whatsapp
    path('', views.home, name='home'),  # Ruta para la página de inicio o cualquier otra vista de 'core'
]


