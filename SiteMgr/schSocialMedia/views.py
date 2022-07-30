from django.http import HttpResponse
from .models import ArticleComments, Article, User
from django.shortcuts import render, redirect
from django.db.models import Q
from .models import ArticleComments, Article, Room, Topic, Message
from .forms import RoomForm, CustomUserCreationForm,UserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm


# Create your views here.

def loginPage(request):

    page = 'login'
    if request.user.is_authenticated:
        return redirect('index')

    if request.method =='POST':
        username = request.POST.get('username').lower()
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, '用户不存在')

        user= authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, '用户或密码不正确')

    context = {'page': page}
    return render(request, 'schSocialMedia/login_register.html', context)


def logoutUser(request):
    logout(request)
    return  redirect('index')

def registerPage(request):
    page ='register'
    form = CustomUserCreationForm()
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request,user)
            return redirect('index')
        else:
            messages.error(request, "注册出现异常")
    context = {'page': page,'form': form}
    return render(request, 'schSocialMedia/login_register.html', context)

def index(request):
    # atcl = Article.objects.get(id=1)
    # cmts = atcl.articlecomments_set.all()[1]
    # atclcmts = ArticleComments.objects.filter(article=atcl)
    # return HttpResponse(atclcmts[0])
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(Q(topic__name__icontains=q) |
                                Q(name__icontains=q) |
                                Q(content__icontains=q)
                                )

    room_count = rooms.count()
    topics = Topic.objects.all()[0:5]
    room_messages = Message.objects.filter(Q(room__topic__name__icontains=q))

    content = {'rooms': rooms,
               'topics': topics,
               'room_count': room_count,
               'room_messages':room_messages}
    return render(request, "schSocialMedia/index.html", content)
    pass


def room(request, pk):
    room = Room.objects.get(id=pk)
    room_messages = room.message_set.all()
    participants = room.participants.all()

    if request.method == 'POST':
        message = Message.objects.create(
            user=request.user,
            room=room,
            content=request.POST.get('body')
        )
        room.participants.add(request.user)
        return redirect('room', pk=room.id)

    content = {'room': room,'room_messages': room_messages,'participants': participants}
    return render(request, "schSocialMedia/room.html", content)

def userProfile(request, pk):
    user = User.objects.get(id=pk)
    rooms = user.room_set.all()
    room_messages = user.message_set.all()

    context = {'user': user ,
               'rooms': rooms,
               'room_messages': room_messages}

    return render(request,'schSocialMedia/profile.html', context)

@login_required(login_url='login')
def createRoom(request):
    form = RoomForm()
    topics = Topic.objects.all()
    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, pub_date = Topic.objects.get_or_create(name=topic_name)
        Room.objects.create(
            host=request.user,
            topic=topic,
            name=request.POST.get('name'),
            content=request.POST.get('content')
        )
        # form = RoomForm(request.POST)
        # if form.is_valid():
        #     room = form.save(commit=False)
        #     room.host = request.user
        #     room.save()
        return redirect('index')

    context = {'form': form,
               'topics': topics}
    return render(request, "schSocialMedia/room_form.html", context)

@login_required(login_url='login')
def updateRoom(request, pk):

    room = Room.objects.get(id=pk)
    form = RoomForm(instance=room)
    topics = Topic.objects.all()
    if request.user != room.host:
        messages.error(request, '不能操作别人的房间')
        return redirect('index')

    if request.method == 'POST':
        topic_name = request.POST.get('topic')
        topic, pub_date = Topic.objects.get_or_create(name=topic_name)
        room.name = request.POST.get('name')
        room.topic = topic
        room.content = request.POST.get('content')
        room.save()
        # form = RoomForm(request.POST, instance=room)
        # if form.is_valid():
        #     form.save()
        return redirect('index')

    context = {'form': form,
               'topics': topics,
               'room': room}
    return render(request, "schSocialMedia/room_form.html", context)

@login_required(login_url='login')
def deleteRoom(request, pk):
    room =Room.objects.get(id=pk)

    if request.user != room.host:
        messages.error(request, '不能操作别人的房间')
        return redirect('index')

    if request.method == 'POST':
        room.delete()
        return redirect('index')

    return render(request, "schSocialMedia/delete.html", {'obj': room})

@login_required(login_url='login')
def deleteMessage(request, pk):
    message =Message.objects.get(id=pk)
    room = message.room
    if request.user != message.user:
        messages.error(request, '不能操作别人的房间')
        return redirect('index')

    if request.method == 'POST':
        message.delete()
        return redirect('index')#redirect(request.META.get('HTTP_REFERER'))
        #redirect(request.META.HTTP_REFERER, pk=room.id)

    return render(request, "schSocialMedia/delete.html", {'obj': message})


@login_required(login_url='login')
def updateUser(request):
    user = request.user
    form = UserForm(instance=user)

    if request.method == 'POST':
        form = UserForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user-profile', pk=user.id)

    contxt ={'form': form}
    return render(request, 'schSocialMedia/edit-user.html',contxt)

def topicsPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    topics = Topic.objects.filter(name__icontains=q)
    contxt ={'topics': topics}
    return render(request, 'schSocialMedia/topics.html', contxt)

def activityPage(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    room_messages = Message.objects.filter(Q(room__name__icontains=q) |
                                           Q(content__icontains=q))
    contxt = {'room_messages': room_messages }
    return render(request, 'schSocialMedia/activity.html', contxt)
