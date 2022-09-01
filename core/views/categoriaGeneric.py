from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaListGeneric(ListCreateAPIView): # GET e POST
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView): # GET<id>, PUT, PATCH e DELETE
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer