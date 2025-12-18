from django.http import HttpResponse

def listar_tarefas(request):
    return HttpResponse("Aqui vão aparecer as tarefas")

def criar_tarefa(request):
    return HttpResponse("Criar tarefa")

def editar_tarefa(request, id):
    return HttpResponse(f"Editar tarefa {id}")

def apagar_tarefa(request, id):
    return HttpResponse(f"Apagar tarefa {id}")

def buscar_tarefas(request):
    return HttpResponse("Buscar tarefas")


# Create your views here.
