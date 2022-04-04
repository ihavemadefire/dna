from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from favorites.models import *
from api.serializers import PirateSerializer


@api_view(['GET', 'POST'])
def pirate_list(request, format=None):
    """
    List all code snippets, or create a new pirate.
    """
    if request.method == 'GET':
        snippets = Pirate.objects.all()
        serializer = PirateSerializer(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PirateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def pirate_detail(request, pk, format=None):
    """
    Retrieve, update or delete a pirate.
    """
    try:
        pirate = Pirate.objects.get(pk=pk)
    except Pirate.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PirateSerializer(pirate)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PirateSerializer(pirate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        pirate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
