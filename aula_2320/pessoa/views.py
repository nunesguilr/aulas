from django.shortcuts import render, redirect
from .models import Pessoa
from .form import PessoaForm

def main(request):
    return render(request, 'pessoa/main.html')

def read(request):
    pessoas = Pessoa.objects.all()
    contexto = {'pessoas': pessoas}
    return render(request, 'pessoa/lista.html', contexto)

def create(request):
    if request.method == 'POST':
        form = PessoaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('read-pessoa')  
    else:
        form = PessoaForm()
    return render(request, 'pessoa/criando.html', {'form': form})

def update(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    
    if request.method == 'POST':
        form = PessoaForm(request.POST, instance=pessoa)
        if form.is_valid():
            form.save()
            return redirect('read-pessoa')  
    else:
        form = PessoaForm(instance=pessoa)    
    return render(request, 'pessoa/atualizando.html', {'form': form})

def delete(request):
    return render(request, 'pessoa/deletando.html')

def detalhe(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
    detalhe = {'pessoa': pessoa} 
    return render(request, 'pessoa/detalhando.html', detalhe)
