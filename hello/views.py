from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

lista = [
    {"id":1,"name":"Nenad"},
    {"id":2,"name":"Ajsela"},
    {"id":3,"name":"Erten"}
]

# Create your views here.
@api_view(['GET'])
def get_all(request):
    return Response(lista)