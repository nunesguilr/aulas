from django.http import HttpResponse
from .models import Pessoa

def main(request):
    return HttpResponse("<h1>seja bem vindo!</h1>")

def read(request):
    pessoas = Pessoa.objects.all()
    html = '<table>'
    html += '<tr><th>Nome</th><th>Idade</th><th>ação</th></tr>'
    
    for pessoa in pessoas:
        html += '<tr>'
        html += '<td>' + pessoa.nome + '</td>'
        html += '<td>' + str(pessoa.idade) + '</td>'
        html += '<td> <a href="/pessoa/' + str(pessoa.id)+ '/">Ver Detalhes</a> </td>'
        html += '</tr>'
    html += '</table>'
        
    return HttpResponse(html)

def create(request):
    return HttpResponse("<h1>criar um novo usuario</h1>")

def update(request):
    return HttpResponse("<h1>atualize usuario</h1>")

def delete(request):
    return HttpResponse("<h1>Delete usuario</h1>")

def detalhe(request, id_pessoa):
    pessoa = Pessoa.objects.get(id=id_pessoa)
        
    html = '<h1>' + pessoa.nome + '</h1>'
    html += 'Idade = ' + str(pessoa.idade)
    
    return HttpResponse("id = " + str(id_pessoa) + " " + html)