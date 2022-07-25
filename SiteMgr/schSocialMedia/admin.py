from django.contrib import admin
from . models import Article, PeopleInfo, ArticleComments, User, Room, Topic, Message
# Register your models here.
admin.site.register(Article)
admin.site.register(PeopleInfo)
admin.site.register(ArticleComments)
admin.site.register(User)
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)


