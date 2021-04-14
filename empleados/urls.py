from rest_framework.urls import path
from empleados.views import VistaEmpleado, DetalleEmpleado

app_name = 'empleados'
urlpatterns = [
    path('', VistaEmpleado.as_view()),
    path('<int:id>', DetalleEmpleado.as_view())
]
