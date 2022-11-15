from django.http import HttpResponse
from django.shortcuts import render
from .forms import CommentForm, ContacForm

def form(request):
    comment_form = CommentForm({'name': 'Alfonso', 'url': 'https://as.com', 'comment': 'comentario'})
    return render(request, 'form.html', {'comment_form': comment_form})

def goal(request):
    if request.method != 'GET':
        return HttpResponse("Método no permitido")

    return HttpResponse(request.GET['name'])

def widget(request):
    if request.method == 'GET':
        form = ContacForm()
        return render(request, 'widget.html', {'form': form}) 

    if request.method == 'POST':
        form = ContacForm(request.POST)
        if form.is_valid():
            return HttpResponse("Válido")
        else:
            return render(request, 'widget.html', {'form': form})      