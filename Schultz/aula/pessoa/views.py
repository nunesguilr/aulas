from django.http import HttpResponse 
from .models import Pessoa

def Index(request):
    return HttpResponse("Vamos iniciar")

def ler(request):
    
    pessoas = Pessoa.objects.all()
    
    tabela = '<table>'
    tabela += '<tr> <th>Nome</th> <th>Idade</th> <th>Desc</th> </tr>'
    
    for pessoa in pessoas:
        tabela += '<tr>'
        tabela += '<td>' + pessoa.nome + '</td>'
        tabela += '<td>' + str(pessoa.idade) + '</td>'
        tabela += '<td> <a href="/pessoa/' + str(pessoa.id)+ '/">Ver Detalhes</a> </td>'
        tabela += '</tr>'
    tabela += '</table>'
    
    return HttpResponse(tabela)

def atualizar(request):
    return HttpResponse("Atualizar um usuário")

def deletar(request):
    return HttpResponse("Deletar usuário")

def detalhar(request, idPessoa):
    pessoa = Pessoa.objects.get(id=idPessoa)
    
    html = '<h2>' + pessoa.nome + '</h2>'
    html += 'Idade = ' + str(pessoa.idade)
    
    return HttpResponse("Detalhes de ID=" + str(idPessoa) + " " + html)