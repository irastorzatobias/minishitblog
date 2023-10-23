from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EntradaListView, EntradaCreateView, EntradaDeleteView, EntradaUpdateView, ComentarioCreateView, ComentarioDeleteView
from .api import CategoriaViewSet, EntradaViewSet, ComentarioViewSet, CustomUserViewSet
from django.contrib.auth.views import LoginView

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'entradas', EntradaViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'usuarios', CustomUserViewSet)

urlpatterns = [
    path('', EntradaListView.as_view(), name='entrada_list'),
    path('entrada/new/', EntradaCreateView.as_view(), name='entrada_new'),
    path('entrada/<int:pk>/delete/', EntradaDeleteView.as_view(), name='entrada_delete'),
    path('entrada/<int:pk>/edit/', EntradaUpdateView.as_view(), name='entrada_edit'),
    path('entrada/<int:pk>/comentario/new/', ComentarioCreateView.as_view(), name='comentario_new'),
    path('comentario/<int:pk>/delete/', ComentarioDeleteView.as_view(), name='comentario_delete'),
    path('login/', LoginView.as_view(template_name="login.html"),name='login'),
    path('api/', include(router.urls)),
]
