from django.contrib import admin
from . models import Article, PeopleInfo, ArticleComments
# Register your models here.
admin.site.register(Article)
admin.site.register(PeopleInfo)
admin.site.register(ArticleComments)


