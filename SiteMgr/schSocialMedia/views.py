
from django.http import HttpResponse
from . models import ArticleComments, Article
from django.shortcuts import render

from .models import ArticleComments, Article


# Create your views here.
rooms = [
    {'id': 1, 'name': 'lets learn python'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

def index(request):
    # atcl = Article.objects.get(id=1)
    # cmts = atcl.articlecomments_set.all()[1]
    # atclcmts = ArticleComments.objects.filter(article=atcl)
    # return HttpResponse(atclcmts[0])
    content = {'rooms': rooms}

    return render(request, "schSocialMedia/index.html", content)
    pass


def room(request, pk):
    return render(request, "schSocialMedia/room.html")

