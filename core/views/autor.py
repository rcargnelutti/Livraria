from rest_framework.viewsets import ModelViewSet

from core.models import Autor
from core.serializers import AuthorSerializer


class AutorViewSet(ModelViewSet):
    queryset = Autor.objects.all()
    serializer_class = AuthorSerializer
    # http_method_names = ['get', 'options', 'head', 'patch', 'post', 'delete']
