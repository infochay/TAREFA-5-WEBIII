from django.urls import path
from .views import (
    TarefaListView,
    TarefaCreateView,
    TarefaUpdateView,
    TarefaDeleteView,
    TarefaSearchView
)

from . import views  # Para a view do formulário DOM

urlpatterns = [
    path('', TarefaListView.as_view(), name='tarefa-lista'),
    path('nova/', TarefaCreateView.as_view(), name='tarefa-nova'),
    path('editar/<int:pk>/', TarefaUpdateView.as_view(), name='tarefa-editar'),
    path('excluir/<int:pk>/', TarefaDeleteView.as_view(), name='tarefa-excluir'),
    path('buscar/', TarefaSearchView.as_view(), name='tarefa-buscar'),

    path('dom/', views.formulario_dom, name='formulario-dom'),

    path('buscar-ajax/', views.buscar_tarefas_ajax, name='buscar-ajax'),
    path('ajax/', views.busca_ajax_view, name='ajax-view'),
]
