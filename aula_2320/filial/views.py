from django.shortcuts import render, redirect
from .models import Filial
from .form import FilialForm

def main(request):
    return render(request, 'filial/main.html')


def read(request):
    filiais = Filial.objects.all()
    contexto = {'filiais': filiais}
    return render(request, 'filial/lista.html', contexto)

def create(request):
    if request.method == 'POST':
        form = FilialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-filial')
    else:
        form = FilialForm()
    return render(request, 'filial/criando.html', {'form': form})

def update(request, id_filial):
    filial = Filial.objects.get(id=id_filial)
    
    if request.method == 'POST':
        form = FilialForm(request.POST, instance=filial)
        if form.is_valid():
            form.save()
            return redirect('read-filial')
    else:
        form = FilialForm(instance=filial)
    return render(request, 'filial/atualizando.html', {'form': form})

def delete(request, id_filial):
    filial = Filial.objects.get(id=id_filial)
    filial.delete() 
    
    return redirect('read-filial')

def detalhe(request, id_filial):
    filial = Filial.objects.get(id=id_filial)
    detalhe = {'filial': filial}
    return render(request, 'filial/detalhando.html', detalhe)
