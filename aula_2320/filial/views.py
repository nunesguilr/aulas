from django.shortcuts import render, redirect, get_object_or_404
from .models import Filial
from .form import FilialForm
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse 


@login_required
def main(request):
    return render(request, 'filial/main.html')

@login_required
def read(request):
    filiais = Filial.objects.all()
    contexto = {'filiais': filiais}
    return render(request, 'filial/lista.html', contexto)

@login_required
def detalhe(request, id_filial):
    filial = get_object_or_404(Filial, id=id_filial) 
    detalhe = {'filial': filial}
    return render(request, 'filial/detalhando.html', detalhe)

@login_required
@permission_required('filial.add_filial', raise_exception=True) 
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
@permission_required('filial.change_filial', raise_exception=True) 
def update(request, id_filial):
    filial = get_object_or_404(Filial, id=id_filial) 

    if request.method == 'POST':
        form = FilialForm(request.POST, instance=filial)
        if form.is_valid():
            form.save()
            return redirect('filial:read')
    else:
        form = FilialForm(instance=filial)
    return render(request, 'filial/atualizando.html', {'form': form})

@login_required
@permission_required('filial.delete_filial', raise_exception=True) #
def delete(request, id_filial):
    filial = get_object_or_404(Filial, id=id_filial) 
    filial.delete()
    return redirect('filial:read')