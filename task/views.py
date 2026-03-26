from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status 
from .models import Kategorija, Obaveza
from .serializers import KategorijaSerializer, ObavezaSerializer

# Create your views here.

@api_view(["GET","POST"])
def get_all_categories(request):
    if request.method == "GET":
        kategorije = Kategorija.objects.all()
        serializer = KategorijaSerializer(kategorije, many=True)
        return Response(serializer.data)
    elif request.method == "POST":
        serializer = KategorijaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET","PUT","PATCH","DELETE"])
def get_category_by_id(request,id):
    try:
        kategorija = Kategorija.objects.get(pk=id)
    except Kategorija.DoesNotExist:
        return Response({"greska":"Kategorija nije pronadjena"},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = KategorijaSerializer(kategorija)
        return Response(serializer.data)
    elif request.method in ["PUT","PATCH"] :
        partial = request.method == "PATCH"
        serializer = KategorijaSerializer(kategorija,data=request.data, partial=partial)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
    elif request.method == "DELETE":
        kategorija.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
# za sledeci cas odraditi views za Obaveze (GET, POST, DELETE, PUT, PATCH)