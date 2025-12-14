from django.urls import path
from .views import (
    FuncionarioCreateView,
    FuncionarioListView,
    FuncionarioUpdateView,
    FuncionarioDeleteView
)

urlpatterns = [
    path('form_funcionario/', FuncionarioCreateView.as_view(), name='form_funcionario'),
    path('lista_funcionarios/', FuncionarioListView.as_view(), name='lista_funcionarios'),
    path('form_funcionario/<int:pk>/', FuncionarioUpdateView.as_view()),
    path('remover_funcionario/<int:pk>/', FuncionarioDeleteView.as_view()),
]
