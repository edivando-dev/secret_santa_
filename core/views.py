from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .forms import GrupoForm
from .models import Grupo


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
 
 
def home(request):
    return render(request, 'home.html')
