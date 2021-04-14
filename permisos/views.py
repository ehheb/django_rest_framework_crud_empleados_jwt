from django.shortcuts import render
from rest_framework import status
from rest_framework.views import Response, APIView
from permisos.models import Permiso
from permisos.serializers import PermisoSerializer, CrearPermisoSerializer


class VistaPermiso(APIView):
    def get(self, request):
        permiso = Permiso.objects.all()
        serialized = PermisoSerializer(permiso, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def post(self, request):
        serialized = CrearPermisoSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DetallePemiso(APIView):
    def get(self, request, id):
        try:
            permiso = Permiso.objects.get(id=id)

        except Permiso.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = CrearPermisoSerializer(permiso)

        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def put(self, request, id):
        try:
            permiso = Permiso.objects.get(id=id)

        except Permiso.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = CrearPermisoSerializer(
            permiso,
            data=request.data
        )

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
            permiso = Permiso.objects.get(id=id)

        except Permiso.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = CrearPermisoSerializer(
            permiso,
            data=request.data,
            partial=True
        )

        if serialized.is_valid():
            serialized.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data,
            )

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            permiso = Permiso.objects.get(id=id)

        except Permiso.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eliminar = permiso.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)