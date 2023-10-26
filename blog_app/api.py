from rest_framework import viewsets
from .models import Categoria, Entrada, Comentario, CustomUser
from .serializers import CategoriaSerializer, EntradaSerializer, ComentarioSerializer, CustomUserSerializer
from rest_framework import permissions, status
from rest_framework.response import Response

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]


class EntradaViewSet(viewsets.ModelViewSet):
    queryset = Entrada.objects.all()
    serializer_class = EntradaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.autor != request.user:
            return Response({"detail": "No tienes permiso para eliminar esta entrada."}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response({"detail": "La entrada se eliminó con éxito."}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.autor != request.user:
            return Response({"detail": "No tienes permiso para actualizar esta entrada."}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer
    permission_classes = [permissions.IsAuthenticated]

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.autor != request.user:
            return Response({"detail": "No tienes permiso para eliminar este comentario."}, status=status.HTTP_403_FORBIDDEN)

        self.perform_destroy(instance)
        return Response({"detail": "El comentario se eliminó con éxito."}, status=status.HTTP_204_NO_CONTENT)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()

        if instance.autor != request.user:
            return Response({"detail": "No tienes permiso para actualizar este comentario."}, status=status.HTTP_403_FORBIDDEN)

        return super().update(request, *args, **kwargs)


class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
