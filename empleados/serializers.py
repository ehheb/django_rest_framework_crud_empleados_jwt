from rest_framework.serializers import ModelSerializer
from empleados.models import Empleado
from puestos.serializers import PuestoSerializer

#Se agrega el serializer del puesto para que se muestre su información
class EmpleadoSerializer(ModelSerializer):
    puesto = PuestoSerializer()
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'apellido', 'edad', 'telefono', 'email', 'puesto')

class CrearEmpleadoSerializer(ModelSerializer):
    class Meta:
        model = Empleado
        fields = ('nombre', 'apellido', 'edad', 'telefono', 'email', 'puesto')
