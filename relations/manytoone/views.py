
from django.shortcuts import render
from django.http import HttpResponse
from .models import Reporter, Article
from datetime import date
# Create your views here.

def create(request):
    rep = Reporter(first_name="Juan", last_name="test", email="test@test.com")
    rep.save()
    art1 = Article(headline="noticias 1", pub_date=date(2022,5,5), reporter=rep)
    art1.save()
    art2 = Article(headline="noticias 2", pub_date=date(2022,6,8), reporter=rep)
    art2.save()
    art3 = Article(headline="noticias 3", pub_date=date(2022,9,12), reporter=rep)
    art3.save()

    #result = art1.reporter.first_name

    #result = rep.article_set.all()

    #result = rep.article_set.filter(headline="noticias 2")

    result = rep.article_set.count()

    return HttpResponse(result)