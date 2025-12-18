from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_tarefas, name='listar_tarefas'),
    path('criar/', views.criar_tarefa, name='criar_tarefa'),
    path('editar/<int:id>/', views.editar_tarefa, name='editar_tarefa'),
    path('apagar/<int:id>/', views.apagar_tarefa, name='apagar_tarefa'),
    path('buscar/', views.buscar_tarefas, name='buscar_tarefas'),
]
