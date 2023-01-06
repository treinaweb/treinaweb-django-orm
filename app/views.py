from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse_lazy, reverse
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

    def post(self, request, *args, **kwargs):
        cliente_form = ClienteForm(data=request.POST)
        endereco_form = EnderecoForm(data=request.POST)
        if cliente_form.is_valid() and endereco_form.is_valid():
            endereco = endereco_form.save()
            cliente = cliente_form.save(commit=False)
            cliente.endereco = endereco
            cliente.save()
            return HttpResponseRedirect(reverse("lista_clientes"))


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
