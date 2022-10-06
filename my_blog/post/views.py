import email
from django.shortcuts import render
from .models import Author, Entry
# Create your views here.

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

    return render(request, 'post/queries.html', {'authors': authors, 'filtered': filtered, 'author': author, 'limits': limits, 'offsets': offsets})

