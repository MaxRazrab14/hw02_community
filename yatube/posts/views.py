from django.shortcuts import render
from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]

    context = {
        'posts': posts
    }
    return render(request, 'posts/index.html', context)


def group_posts(request, slug):
    group = Group.objects.get(slug=slug)
    posts = group.group_posts.all()[:10]
    context = {
        'group': group,
        'posts': posts
    }
    return render(request, 'posts/group_list.html', context)
