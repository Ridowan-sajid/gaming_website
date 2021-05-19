from urllib import request
from django.shortcuts import render
from game.models import Game


def home(request):
    posts = Game.objects.all()
    context = {
        "posts": posts
    }

    return render(request, "game/home.html", context)

def gamingPost(request,pk):
    post=Game.objects.get(id=pk)
    context={
        "post":post
    }

    return render(request,"game/game_details.html",context)
