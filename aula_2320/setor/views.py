from django.shortcuts import render, redirect
from .models import Setor
from .form import SetorForm

def main(request):
    return render(request, 'setor/main.html')


def read(request):
    setores = Setor.objects.all()
    contexto = {'setores': setores}
    return render(request, 'setor/lista.html', contexto)

def create(request):
    if request.method == 'POST':
        form = SetorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-setor')
    else:
        form = SetorForm()
    return render(request, 'setor/criando.html', {'form': form})

def update(request, id_setor):
    setor = Setor.objects.get(id=id_setor)
    
    if request.method == 'POST':
        form = SetorForm(request.POST, instance=setor)
        if form.is_valid():
            form.save()
            return redirect('read-setor')
    else:
        form = SetorForm(instance=setor)
    return render(request, 'setor/atualizando.html', {'form': form})

def delete(request, id_setor):
    setor = Setor.objects.get(id=id_setor)
    setor.delete() 
    
    return redirect('read-setor')

def detalhe(request, id_setor):
    setor = Setor.objects.get(id=id_setor)
    detalhe = {'setor': setor}
    return render(request, 'setor/detalhando.html', detalhe)
