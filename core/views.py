from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.views.generic import CreateView, DetailView
from .forms import GrupoForm
from .models import Grupo
import random


@login_required
def realizar_sorteio(request, pk):
    if request.method == 'POST':
        try:
            grupo = Grupo.objects.get(pk=pk)
            participantes = list(grupo.participantes.all())
            if len(participantes) < 2:
                messages.error(request, "O sorteio requer pelo menos 2 participantes")
                return redirect('home')
            
            sorteados = list(participantes)
            sorteio_valido = False
            while not sorteio_valido:
                random.shuffle(sorteados)
                sorteio_valido = True
                for i in range(len(participantes)):
                    if participantes[i] == sorteados[i]:
                        sorteio_valido = False
                        break
            for i in range(len(participantes)):
                participantes_atual = participantes[i]
                participantes_atual.sorteado = sorteados[i]
                participantes_atual.save()

            messages.success(request, f"Sorteio do grupo '{grupo.nome}' realizado com sucesso!")
        except Grupo.DoesNotExist:
            messages.error(request, "Este grupo não existe.")
        return redirect('home')


# Create your views here.

"""@login_required

def criar_grupo(request):
    if request.method == 'POST':
        form = GrupoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GrupoForm()
        return render(request, 'core/criar_grupo.html', {'form': form})
     """
    
class GrupoCreateView(LoginRequiredMixin, CreateView):
    model = Grupo
    form_class = GrupoForm
    template_name = 'core/criar_grupo.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, f"O grupo '{self.object.nome}' foi criado com sucesso!")
        return response
 

class GrupoDetailView(LoginRequiredMixin, DetailView):
    model = Grupo
    template_name = 'core/grupo_detail.html'
    context_object_name= 'grupo'

def home(request):
    grupos = Grupo.objects.all()
    context = {
        'grupos': grupos
    }
    return render(request, 'home.html')
