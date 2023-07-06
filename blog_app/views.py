from .models import Entrada, Comentario

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
# from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import EntradaForm


class EntradaListView(ListView):
    model = Entrada
    template_name = 'blog_app/entrada_list.html'


class EntradaCreateView(CreateView):
    form_class = EntradaForm
    template_name = 'blog_app/entrada_form.html'
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)


class EntradaUpdateView(UpdateView):
    model = Entrada
    form_class = EntradaForm
    template_name = 'blog_app/entrada_update.html'
    success_url = reverse_lazy('entrada_list')


class EntradaDeleteView(DeleteView):
    model = Entrada
    success_url = reverse_lazy('entrada_list')


class ComentarioCreateView(CreateView):
    model = Comentario
    fields = ['texto']
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.entrada = Entrada.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)


class ComentarioDeleteView(DeleteView):
    model = Comentario
    success_url = reverse_lazy('entrada_list')
