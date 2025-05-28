from django.shortcuts import render, redirect, get_object_or_404
from .models import Setor
from .form import SetorForm
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse # Importe reverse para redirecionamentos nomeados

@login_required
def main(request):
    return render(request, 'setor/main.html')

@login_required
def read(request):
    setores = Setor.objects.all()
    contexto = {'setores': setores}
    return render(request, 'setor/lista.html', contexto)

@login_required
def detalhe(request, id_setor):
    setor = get_object_or_404(Setor, id=id_setor) 
    detalhe = {'setor': setor}
    return render(request, 'setor/detalhando.html', detalhe)

@login_required
@permission_required('setor.add_setor', raise_exception=True) 
def create(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('setor:read')
    else:
        form = SetorForm()
    return render(request, 'setor/criando.html', {'form': form})

@login_required
@permission_required('setor.change_setor', raise_exception=True) 
def update(request, id_setor):
    setor = get_object_or_404(Setor, id=id_setor) 

    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            return redirect('setor:read')
    else:
        form = SetorForm(instance=setor)
    return render(request, 'setor/atualizando.html', {'form': form})

@login_required
@permission_required('setor.delete_setor', raise_exception=True) 
def delete(request, id_setor):
    setor = get_object_or_404(Setor, id=id_setor) 
    setor.delete()
    return redirect('setor:read')