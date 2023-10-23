from rest_framework import viewsets
from .models import Categoria, Entrada, Comentario, CustomUser
from .serializers import CategoriaSerializer, EntradaSerializer, ComentarioSerializer, CustomUserSerializer
from rest_framework import permissions

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    permission_classes = [permissions.IsAuthenticated]

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
