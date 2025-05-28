from django.shortcuts import render, redirect, get_object_or_404
from .models import Pessoa
from .form import PessoaForm
from django.contrib.auth.decorators import login_required, permission_required
from django.urls import reverse


@login_required
def main(request):
    return render(request, 'pessoa/main.html')

@login_required
def read(request):
    pessoas = Pessoa.objects.all()
    contexto = {'pessoas': pessoas}
    return render(request, 'pessoa/lista.html', contexto)

@login_required
def detalhe(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    detalhe = {'pessoa': pessoa}
    return render(request, 'pessoa/detalhando.html', detalhe)

@login_required
@permission_required('pessoa.add_pessoa', raise_exception=True) 
def create(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pessoa:read')
    else:
        form = PessoaForm()
    return render(request, 'pessoa/criando.html', {'form': form})

@login_required
@permission_required('pessoa.change_pessoa', raise_exception=True) 
def update(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)

    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa:read')
    else:
        form = PessoaForm(instance=pessoa)
    return render(request, 'pessoa/atualizando.html', {'form': form})

@login_required
@permission_required('pessoa.delete_pessoa', raise_exception=True) 
def delete(request, id_pessoa):
    pessoa = get_object_or_404(Pessoa, id=id_pessoa)
    pessoa.delete()
    return redirect('pessoa:read')