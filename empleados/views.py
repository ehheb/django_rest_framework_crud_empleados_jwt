from django.shortcuts import render
from rest_framework import status
from rest_framework.views import Response, APIView
from empleados.models import Empleado
from empleados.serializers import EmpleadoSerializer, CrearEmpleadoSerializer

class VistaEmpleado(APIView):
    def get(self, request):
        empleado = Empleado.objects.all()
        serialized = EmpleadoSerializer(empleado, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def post(self, request):
        serialized = CrearEmpleadoSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_201_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DetalleEmpleado(APIView):

    def get(self, request, id):
        try:
            empleado = Empleado.objects.get(id=id)

        except Empleado.DoesNotExist:
            return Response(stats=status.HTTP_404_NOT_FOUND)

        serialized = EmpleadoSerializer(empleado)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def put(self, request, id):
        try:
            empleado = Empleado.objects.get(id=id)

        except Empleado.DoesNotExist:
            return Response(stats=status.HTTP_404_NOT_FOUND)

        serialized = CrearEmpleadoSerializer(empleado, data=request.data)
        print(serialized)
        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


    def patch(self, request, id):
        try:
            empleado = Empleado.objects.get(id=id)

        except Empleado.DoesNotExist:
            return Response(stats=status.HTTP_404_NOT_FOUND)

        serialized = CrearEmpleadoSerializer(
            empleado,
            data=request.data,
            partial=True
        )

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            empleado = Empleado.objects.get(id=id)

        except Empleado.DoesNotExist:
            return Response(stats=status.HTTP_404_NOT_FOUND)

        eliminar = empleado.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
