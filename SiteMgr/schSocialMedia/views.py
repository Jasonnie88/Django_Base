from django.http import HttpResponse
from .models import ArticleComments, Article
from django.shortcuts import render, redirect

from .models import ArticleComments, Article, Room
from .forms import RoomForm


# Create your views here.
# rooms = [
#     {'id': 1, 'name': 'lets learn python'},
#     {'id': 2, 'name': 'Design with me'},
#     {'id': 3, 'name': 'Frontend developers'},
# ]

def index(request):
    # atcl = Article.objects.get(id=1)
    # cmts = atcl.articlecomments_set.all()[1]
    # atclcmts = ArticleComments.objects.filter(article=atcl)
    # return HttpResponse(atclcmts[0])
    rooms = Room.objects.all()
    content = {'rooms': rooms}
    return render(request, "schSocialMedia/index.html", content)
    pass


def room(request, pk):
    room = Room.objects.get(id=pk)
    content = {'room': room}
    return render(request, "schSocialMedia/room.html", content)


def createRoom(request):
    form = RoomForm()
    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, "schSocialMedia/room_form.html", context)


def updateRoom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)

    if request.method == 'POST':
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('index')

    context = {'form': form}
    return render(request, "schSocialMedia/room_form.html", context)

def deleteRoom(request, pk):
    room =Room.objects.get(id=pk)
    if request.method == 'POST':
        room.delete()
        return redirect('index')

    return render(request, "schSocialMedia/delete_room.html", {'obj': room})
