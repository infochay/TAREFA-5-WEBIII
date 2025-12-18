from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.http import JsonResponse
from .models import Tarefa

# Listar tarefas
class TarefaListView(ListView):
    model = Tarefa
    template_name = "tarefas/tarefa_lista.html"

# Criar tarefa
class TarefaCreateView(CreateView):
    model = Tarefa
    template_name = "tarefas/tarefa_form.html"
    fields = ['titulo', 'descricao', 'concluida']
    success_url = reverse_lazy('tarefa-lista')

# Editar tarefa
class TarefaUpdateView(UpdateView):
    model = Tarefa
    template_name = "tarefas/tarefa_form.html"
    fields = ['titulo', 'descricao', 'concluida']
    success_url = reverse_lazy('tarefa-lista')

# Apagar tarefa
class TarefaDeleteView(DeleteView):
    model = Tarefa
    template_name = "tarefas/tarefa_confirm_delete.html"
    success_url = reverse_lazy('tarefa-lista')

# Buscar tarefas (form tradicional)
class TarefaSearchView(ListView):
    model = Tarefa
    template_name = "tarefas/tarefa_buscar.html"

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Tarefa.objects.filter(titulo__icontains=query)
        return Tarefa.objects.all()

# =========================
# FORMULÁRIO DOM (JS)
# =========================
def formulario_dom(request):
    return render(request, "tarefas/form_dom.html")

# =========================
# PÁGINA AJAX
# =========================
def busca_ajax_view(request):
    return render(request, "tarefas/busca_ajax.html")

# =========================
# AJAX - BUSCA ASSÍNCRONA
# =========================
def buscar_tarefas_ajax(request):
    termo = request.GET.get("q", "")
    tarefas = Tarefa.objects.filter(titulo__icontains=termo)

    dados = [
        {"id": t.id, "titulo": t.titulo}
        for t in tarefas
    ]
    return JsonResponse(dados, safe=False)
