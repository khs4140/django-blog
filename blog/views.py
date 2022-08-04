from django.shortcuts import render

from blog.models import Post

from .models import Post
# Create your views here.


def index(request):
    posts = Post.objects.all().order_by('-pk')

    return render(
        request,
        './blog/index.html',
        {
            'posts': posts,
        }
    )


def single_post_page(request, pk):
    post = Post.objects.all().get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )
