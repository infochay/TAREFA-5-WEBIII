from django.urls import path
from .views import (
    TarefaListView,
    TarefaCreateView,
    TarefaUpdateView,
    TarefaDeleteView,
    TarefaSearchView
)

urlpatterns = [
    path('', TarefaListView.as_view(), name='tarefa-lista'),
    path('nova/', TarefaCreateView.as_view(), name='tarefa-nova'),
    path('editar/<int:pk>/', TarefaUpdateView.as_view(), name='tarefa-editar'),
    path('excluir/<int:pk>/', TarefaDeleteView.as_view(), name='tarefa-excluir'),
    path('buscar/', TarefaSearchView.as_view(), name='tarefa-buscar'),
]
