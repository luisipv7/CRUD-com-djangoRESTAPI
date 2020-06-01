from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from app.models import Contato
from app.serializers import ContatoSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def contato_list(request):
    if request.method == 'GET':
      contatos = Contato.objects.all()

      nome = request.GET.get('nome', None)
      if nome is not None:

        contatos = contatos.filter(nome__icontains=nome)

      contato_serializer = ContatoSerializer(contatos, many=True)
      return JsonResponse(contato_serializer.data, safe=False)
            # 'safe=False' for objects serialization
        # GET list of tutorials, POST a new tutorial, DELETE all tutorials
    elif request.method == 'POST':
        contatos_data = JSONParser().parse(request)
        contato_serializer = ContatoSerializer(data=contatos_data)
        if contato_serializer.is_valid():
            contato_serializer.save()
            return JsonResponse(contato_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(contato_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      count = Contato.objects.all().delete()
      return JsonResponse({'message': '{} Contatos were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def contato_detail(request, pk):
    # find tutorial by pk (id)
    try:
      contatos = Contato.objects.get(pk=pk)
    except Contato.DoesNotExist:
      return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET / PUT / DELETE tutorial

    if request.method == 'GET':
      contato_serializer = ContatoSerializer(contatos)
      return JsonResponse(contato_serializer.data)

    elif request.method == 'PUT':
      contatos_data = JSONParser().parse(request)
      contatos_serializer = ContatoSerializer(contatos, data=contatos_data)
      if contatos_serializer.is_valid():
        contatos_serializer.save()
        return JsonResponse(contatos_serializer.data)
      return JsonResponse(contatos_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
      contatos.delete()
      return JsonResponse({'message': 'Contato was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def contato_list_published(request):
  # GET all published tutorials
  contatos = Contato.objects.filter(ativo=True)

  if request.method == 'GET':
      contatos_serializer = ContatoSerializer(contatos, many=True)
      return JsonResponse(contatos_serializer.data, safe=False)
