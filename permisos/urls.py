from permisos.views import VistaPermiso, DetallePemiso
from rest_framework.urls import path

app_name = 'permisos'

urlpatterns = [
    path('', VistaPermiso.as_view()),
    path('<int:id>', DetallePemiso.as_view())
]
