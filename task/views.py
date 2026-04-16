from django.shortcuts import render
from .models import Kategorija, Obaveza
from .serializers import KategorijaSerializer, ObavezaSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
# Create your views here.

# class CategoryListCreateView(ListCreateAPIView):
#     queryset = Kategorija.objects.all()
#     serializer_class = KategorijaSerializer
    

# class CategoryDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Kategorija.objects.all()
#     serializer_class = KategorijaSerializer
    
class CategoryViewSet(ModelViewSet):
    queryset = Kategorija.objects.all()
    serializer_class = KategorijaSerializer
        
class TaskViewSet(ModelViewSet):
    queryset = Obaveza.objects.all()
    serializer_class = ObavezaSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ["zavrseno","prioritet","kategorija"]
    search_fields = ["naslov", "opis"]
    ordering_fields = ["kreirano", "rok_za_zavrsetak", "prioritet"]
    ordering = ["-kreirano"]
    
# @api_view(["GET","POST"])
# def get_all_categories(request):
#     if request.method == "GET":
#         if request.GET.get("naziv"):
#             kategorije = Kategorija.objects.filter(naziv=request.GET.get("naziv"))
#         else:
#             kategorije = Kategorija.objects.all()
            
#         if request.GET.get("opis"):
#             kategorije = kategorije.filter(opis__icontains=request.GET.get("opis"))
        
#         serializer = KategorijaSerializer(kategorije, many=True)
#         return Response(serializer.data)
#     elif request.method == "POST":
#         serializer = KategorijaSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(["GET","PUT","PATCH","DELETE"])
# def get_category_by_id(request,id):
#     try:
#         kategorija = Kategorija.objects.get(pk=id)
#     except Kategorija.DoesNotExist:
#         return Response({"greska":"Kategorija nije pronadjena"},status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == "GET":
#         serializer = KategorijaSerializer(kategorija)
#         return Response(serializer.data)
#     elif request.method in ["PUT","PATCH"] :
#         partial = request.method == "PATCH"
#         serializer = KategorijaSerializer(kategorija,data=request.data, partial=partial)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#     elif request.method == "DELETE":
#         kategorija.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
        
# za sledeci cas odraditi views za Obaveze (GET, POST, DELETE, PUT, PATCH)
# class ObavezaListCreateView(ListCreateAPIView):
#     queryset = Obaveza.objects.all()
#     serializer_class = ObavezaSerializer
    # def get(self, request):
    #     obaveze = Obaveza.objects.all()
    #     serializer = ObavezaSerializer(obaveze, many=True)
    #     return Response(serializer.data)

    # def post(self, request):
    #     serializer = ObavezaSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# class ObavezaDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = Obaveza.objects.all()
#     serializer_class = ObavezaSerializer
    
# class ObavezaDetailView(APIView):
#     def get_object(self, id):
#         try:
#             return Obaveza.objects.get(pk=id)
#         except Obaveza.DoesNotExist:
#             raise Http404

#     def get(self, request, id):
#         obaveza = self.get_object(id)
#         serializer = ObavezaSerializer(obaveza)
#         return Response(serializer.data)

#     def put(self, request, id):
#         obaveza = self.get_object(id)
#         serializer = ObavezaSerializer(obaveza, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def patch(self, request, id):
#         obaveza = self.get_object(id)
#         serializer = ObavezaSerializer(obaveza, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def delete(self, request, id):
#         obaveza = self.get_object(id)
#         obaveza.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)