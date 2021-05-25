from urllib import request
from django.shortcuts import render
from game.models import Game, Comment
from game.forms import GameForm
from django.core.paginator import Paginator


def home(request):
    posts = Game.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "page_obj": page_obj,
    }

    return render(request, "game/home.html", context)


def action(request):
    posts = Game.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "page_obj": page_obj,
    }

    return render(request, "game/action.html", context)


def action_adventure(request):
    posts = Game.objects.all()
    paginator = Paginator(posts, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        "posts": posts,
        "page_obj": page_obj,
    }

    return render(request, "game/action-adventure.html", context)


def gamingPost(request, pk):
    post = Game.objects.get(id=pk)
    comment = Comment.objects.all()
    # images=GameImage.objects.all()
    comment_form = GameForm()
    if request.method == "POST":
        comment_form = GameForm(request.POST)
        if comment_form.is_valid():
            Comment.objects.create(
                game=post,
                game_comment=comment_form.cleaned_data.get('game_comment'),
                commenter=request.user
            )
            comment_form = GameForm()
    context = {
        "post": post,
        "comment_form": comment_form,
        "comment": comment,
        # "images":images
    }

    return render(request, "game/game_details.html", context)

# def gaming_comment(request):
#     comment_form=GameForm()
#     if request.method == "POST":
#         comment_form = GameForm(request.POST)
#         if comment_form.is_valid():
#             Comment.objects.create(**comment_form)
#
#     context={
#         "comment_form":comment_form,
#     }
#
#     return render(request,"game/game_details.html",context)
