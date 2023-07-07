from django.urls import path
from .views import EntradaListView, EntradaCreateView, EntradaDeleteView, EntradaUpdateView, ComentarioCreateView, ComentarioDeleteView

urlpatterns = [
    path('', EntradaListView.as_view(), name='entrada_list'),
    path('entrada/new/', EntradaCreateView.as_view(), name='entrada_new'),
    path('entrada/<int:pk>/delete/',
         EntradaDeleteView.as_view(), name='entrada_delete'),
    path('entrada/<int:pk>/edit/', EntradaUpdateView.as_view(), name='entrada_edit'),
    path('entrada/<int:pk>/comentario/new/',
         ComentarioCreateView.as_view(), name='comentario_new'),
    path('comentario/<int:pk>/delete/',
         ComentarioDeleteView.as_view(), name='comentario_delete'),
]
