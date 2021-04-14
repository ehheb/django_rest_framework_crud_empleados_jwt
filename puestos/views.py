from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.views import APIView, Response
from puestos.models import Puesto
from puestos.serializers import PuestoSerializer

class VistaPuesto(APIView):

    def get(self, request):
        puesto = Puesto.objects.all()
        serialized = PuestoSerializer(puesto, many=True)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def post(self, request):
        serialized = PuestoSerializer(data=request.data)

        if serialized.is_valid():
            serialized.save()
            return Response(
                status=status.HTTP_201_CREATED,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class DetallePuesto(APIView):

    def get(self, request, id):
        try:
            puesto = Puesto.objects.get(id=id)

        except Puesto.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = PuestoSerializer(puesto)
        return Response(
            status=status.HTTP_200_OK,
            data=serialized.data
        )

    def put(self, request, id):
        try:
            puesto = Puesto.objects.get(id=id)

        except Puesto.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = PuestoSerializer(puesto, data=request.data)

        print(serialized)
        if serialized.is_valid():
            serialized.save()

            return Response(
                status=status.HTTP_200_OK,
                data=serialized.data
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    #Realmente en este caso el patch no tiene caso ponerlo
    #ya que esta app (puestos) contiene un solo atributo llamado nombre
    #sin embargo, se colocó para fines de aprendizaje
    def patch(self, request, id):
        try:
            puesto = Puesto.objects.get(id=id)

        except Puesto.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        serialized = PuestoSerializer(
            puesto,
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
            puesto = Puesto.objects.get(id=id)

        except Puesto.DoesNotExist:
            return Response(status=status.HTTP_400_BAD_REQUEST)

        eliminar = puesto.delete()

        if eliminar:
            return Response(status=status.HTTP_204_NO_CONTENT)

        else: return Response(status=status.HTTP_400_BAD_REQUEST)
