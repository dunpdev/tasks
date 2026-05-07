from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .tasks import notify_user
lista = [
    {"id":1,"name":"Nenad"},
    {"id":2,"name":"Ajsela"},
    {"id":3,"name":"Erten"}
]

# Create your views here.
@api_view(['GET'])
def get_all(request):
    notify_user.delay("Hello from Celery!")
    return Response(lista)