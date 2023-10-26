from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from .models import Categoria, Entrada, Comentario, CustomUser
from .serializers import CategoriaSerializer, EntradaSerializer, ComentarioSerializer, CustomUserSerializer

class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.autor != request.user:
            return Response({"detail": "No tienes permiso para eliminar este objeto."}, status=status.HTTP_403_FORBIDDEN)
        self.perform_destroy(instance)
        return Response({"detail": "El objeto se eliminó con éxito."}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.autor != request.user:
            return Response({"detail": "No tienes permiso para actualizar este objeto."}, status=status.HTTP_403_FORBIDDEN)
        return super().update(request, *args, **kwargs)

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntradaViewSet(BaseViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer

class ComentarioViewSet(BaseViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    permission_classes = [permissions.IsAuthenticated]
