from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from .forms import EntradaForm
from .models import Entrada, Comentario

class EntradaListView(ListView):
    model = Entrada
    template_name = 'blog_app/entrada_list.html'

class EntradaCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = EntradaForm
    template_name = 'blog_app/entrada_form.html'
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        return super().form_valid(form)

class EntradaUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    model = Entrada
    form_class = EntradaForm
    template_name = 'blog_app/entrada_update.html'
    success_url = reverse_lazy('entrada_list')

class EntradaDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Entrada
    success_url = reverse_lazy('entrada_list')

class ComentarioCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    model = Comentario
    fields = ['texto']
    success_url = reverse_lazy('entrada_list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        form.instance.entrada = Entrada.objects.get(id=self.kwargs['pk'])
        return super().form_valid(form)

class ComentarioDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Comentario
    success_url = reverse_lazy('entrada_list')
