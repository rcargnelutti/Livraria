from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView # noqa W292
from core.models import Categoria
from core.serializers import CategoriaSerializer


class CategoriaListGeneric(ListCreateAPIView): # GET e POST # noqa E261
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaDetailGeneric(RetrieveUpdateDestroyAPIView): # GET<id>, PUT, PATCH e DELETE # noqa E261
    lookup_field = 'id'
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer # noqa W292