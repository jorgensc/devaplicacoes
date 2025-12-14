from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Funcionario

class FuncionarioCreateView(CreateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

class FuncionarioListView(ListView):
    model = Funcionario
    template_name = "lista_funcionarios.html"

class FuncionarioUpdateView(UpdateView):
    model = Funcionario
    fields = "__all__"
    template_name = "form_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")

class FuncionarioDeleteView(DeleteView):
    model = Funcionario
    template_name = "remover_funcionario.html"
    success_url = reverse_lazy("lista_funcionarios")
