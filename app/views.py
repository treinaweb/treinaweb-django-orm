from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView
from .models import Cliente
from .forms import ClienteForm, EnderecoForm

# Create your views here.


class ClienteCreateView(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = "form_cliente.html"
    success_url = "lista_clientes"

    def get_context_data(self, **kwargs):
        context = super(ClienteCreateView, self).get_context_data(**kwargs)
        context["form"] = ClienteForm()
        context["endereco_form"] = EnderecoForm()
        return context


class ClienteListView(ListView):
    model = Cliente
    template_name = "lista_clientes.html"

# Adicionar um comentário
class ClienteDetailView(DetailView):
    model = Cliente
    template_name = "lista_cliente.html"
    context_object_name = "cliente"


class ClienteUpdateView(UpdateView):
    model = Cliente
    fields = ("nome", "profissao", "data_nascimento")
    template_name = "form_cliente.html"
    success_url = reverse_lazy("lista_clientes")


class ClienteDeleteView(DeleteView):
    model = Cliente
    template_name = "remover_cliente.html"
    success_url = reverse_lazy("lista_clientes")
