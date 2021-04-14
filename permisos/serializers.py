from rest_framework.serializers import ModelSerializer

from empleados.serializers import EmpleadoSerializer
from permisos.models import Permiso

#Se agrega el serializer del empleado para que este se muestre
class PermisoSerializer(ModelSerializer):
    empleado = EmpleadoSerializer()
    class Meta:
        model = Permiso
        fields = ('id', 'nombre', 'empleado')

class CrearPermisoSerializer(ModelSerializer):
    class Meta:
        model = Permiso
        fields = ('nombre', 'empleado')
