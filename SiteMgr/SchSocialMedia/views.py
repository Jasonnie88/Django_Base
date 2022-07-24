from django.http import HttpResponse
from . models import ArticleComments, Article
from django.http import HttpResponse

from .models import ArticleComments, Article


# Create your views here.

def index(request):
    atcl = Article.objects.get(id=1)
    cmts = atcl.articlecomments_set.all()[1]
    atclcmts = ArticleComments.objects.filter(article=atcl)
    return HttpResponse(atclcmts[0])
    pass

