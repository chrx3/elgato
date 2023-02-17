from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from Gato.models import Usuario, Gatito
from Gato.serializers import GatitoSerializer,UsuarioSerializer
from drf_spectacular.utils import extend_schema, extend_schema_view
from rest_framework import viewsets
# Create your views here.
from django.core.files.storage import default_storage

@extend_schema_view(
    list=extend_schema(description='Permite obtener una lista de tareas'),
    retrieve=extend_schema(description='Permite obtener una tarea'),
    create=extend_schema(description='Permite crear una tarea'),
    upgrade=extend_schema(description='Permite actualizar una tarea'),
    destroy=extend_schema(description='Permite eliminar una tarea'),
)
class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()

class GatoViewSet(viewsets.ModelViewSet):
    serializer_class = GatitoSerializer
    queryset = Gatito.objects.all()





# @csrf_exempt
# def usuarioAPI(request, id=0):
#     if request.method=='GET':
#         usuario = Usuario.objects.all()
#         usuario_serializer=UsuarioSerializer(usuario,many=True)
#         return JsonResponse(usuario_serializer.data, safe=False)
#     elif request.method=='POST':
#         usuarios_data= JSONParser().parse(request)
#         usuario_serializer=UsuarioSerializer(data=usuarios_data)
#         if usuario_serializer.is_valid():
#             usuario_serializer.save()
#             return JsonResponse("Agregado",safe=False)
#         return JsonResponse("Fallo", safe=False)
#     elif request.method=='PUT':
#         usuario_data=JSONParser().parse(request)
#         usuario = Usuario.objects.get(Id=usuario_data['Id'])
#         usuario_serializer = UsuarioSerializer(usuario,data=usuario_data)
#         if usuario_serializer.is_valid():
#             usuario_serializer.save()
#             return JsonResponse("Actualizado",safe=False)
#         return JsonResponse('Fallo la actualizacion')
#     elif request.method=='DELETE':
#         usuario=Usuario.objects.get(Id=id)
#         usuario.delete()
#         return JsonResponse("Eliminado",safe=False)


# @csrf_exempt
# def gatitoAPI(request, id=0):
#     if request.method=='GET':
#         gatito = Gatito.objects.all()
#         gatito_serializer=GatitoSerializer(gatito,many=True)
#         return JsonResponse(gatito_serializer.data, safe=False)
#     elif request.method=='POST':
#         gatito_data= JSONParser().parse(request)
#         gatito_serializer=GatitoSerializer(data=gatito_data)
#         if gatito_serializer.is_valid():
#             gatito_serializer.save()
#             return JsonResponse("Agregado",safe=False)
#         return JsonResponse("Fallo", safe=False)
#     elif request.method=='PUT':
#         gatito_data=JSONParser().parse(request)
#         gatito = Gatito.objects.get(id=gatito_data['id'])
#         gatito_serializer = GatitoSerializer(gatito,data=gatito_data)
#         if gatito_serializer.is_valid():
#             gatito_serializer.save()
#             return JsonResponse("Actualizado",safe=False)
#         return JsonResponse('Fallo la actualizacion')
#     elif request.method=='DELETE':
#         gatito_serializer=Gatito.objects.get(Id=id)
#         gatito_serializer.delete()
#         return JsonResponse("Eliminado",safe=False)

@csrf_exempt
def SaveFile(request):
    file=request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name,safe=False)