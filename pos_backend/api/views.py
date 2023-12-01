from rest_framework import generics

from .models import (
    Mesa,Categoria
)

from .serializers import (
    CategoriaSerializer,
    MesaSerializer
)

class CategoriaView(generics.ListAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    
class MesaView(generics.ListAPIView):
    queryset = Mesa.objects.all()
    serializer_class = MesaSerializer