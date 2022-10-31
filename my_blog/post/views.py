import email
from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Entry
# Create your views here.

def update(request):
    author = Author.objects.get(id=1)
    author.name = "Juanjo"
    author.email ="juanjo@demo.com"
    author.save()
    return HttpResponse("Modificado")

def queries(request):
    # get all the elements
    authors = Author.objects.all()

    # get filtered elements by condition
    filtered = Author.objects.filter(email='ryan24@example.org')

    # get an unique object
    author = Author.objects.get(id=1)

    # get the first 10 objects
    limits = Author.objects.all()[:10]

    # get the first 5 elements avoiding the first 5 elements
    offsets = Author.objects.all()[5:10]

    # get all the elements organized by email
    organized = Author.objects.all().order_by('email')

    # get all the elements filtered by id lower than equals 15
    filtered2 = Author.objects.filter(id__lte=15)

    # obtain all the authors that contains the word yes
    filtered3 = Author.objects.filter(name__contains="yes")



    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets, 'organized': organized, 'filtered2': filtered2, 'filtered3':filtered3})

