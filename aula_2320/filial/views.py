from django.shortcuts import render, redirect
from .models import Filial
from .form import FilialForm
from django.contrib.auth.decorators import login_required 

@login_required 
def main(request):
    return render(request, 'filial/main.html')


@login_required 
def read(request):
    filiais = Filial.objects.all()
    contexto = {'filiais': filiais}
    return render(request, 'filial/lista.html', contexto)

@login_required 
def create(request):
    if request.method == 'POST':
        form = FilialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('filial:read')
    else:
        form = FilialForm()
    return render(request, 'filial/criando.html', {'form': form})

@login_required 
def update(request, id_filial):
    filial = Filial.objects.get(id=id_filial)
    
    if request.method == 'POST':
        form = FilialForm(request.POST, instance=filial)
        if form.is_valid():
            form.save()
            return redirect('filial:read')
    else:
        form = FilialForm(instance=filial)
    return render(request, 'filial/atualizando.html', {'form': form})

@login_required 
def delete(request, id_filial):
    filial = Filial.objects.get(id=id_filial)
    filial.delete() 
    
    return redirect('filial:read')

@login_required 
def detalhe(request, id_filial):
    filial = Filial.objects.get(id=id_filial)
    detalhe = {'filial': filial}
    return render(request, 'filial/detalhando.html', detalhe)
