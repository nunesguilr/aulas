from django.shortcuts import render, redirect
from .models import Pessoa
from .form import PessoaForm
from django.contrib.auth.decorators import login_required 

@login_required 
def main(request):
    return render(request, 'pessoa/main.html')


@login_required 
def read(request):
    pessoas = Pessoa.objects.all()
    contexto = {'pessoas': pessoas}
    return render(request, 'pessoa/lista.html', contexto)

@login_required 
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
def update(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('pessoa:read') 
    else:
        form = PessoaForm(instance=pessoa)    
    return render(request, 'pessoa/atualizando.html', {'form': form})

@login_required 
def delete(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    pessoa.delete() 
    
    return redirect('pessoa:read') 

@login_required 
def detalhe(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    detalhe = {'pessoa': pessoa} 
    return render(request, 'pessoa/detalhando.html', detalhe)
