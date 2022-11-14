from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm

def form(request):
    comment_form = CommentForm({'name': 'Alfonso', 'url': 'https://as.com', 'comment': 'comentario'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != 'GET':
        return HttpResponse("Método no permitido")

    return HttpResponse(request.GET['name'])