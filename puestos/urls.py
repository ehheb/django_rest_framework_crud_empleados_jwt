from rest_framework.urls import path
from puestos.views import VistaPuesto, DetallePuesto

app_name = 'puestos'

urlpatterns = [
    path('', VistaPuesto.as_view()),
    path('<int:id>', DetallePuesto.as_view())
]
