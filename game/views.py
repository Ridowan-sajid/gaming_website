from urllib import request
from django.shortcuts import render
from game.models import Game,GameImage


def home(request):
    posts = Game.objects.all()
    context = {
        "posts": posts
    }

    return render(request, "game/home.html", context)

def gamingPost(request,pk):
    post=Game.objects.get(id=pk)
    images=GameImage.objects.all()
    context={
        "post":post,
        "images":images
    }

    return render(request,"game/game_details.html",context)
