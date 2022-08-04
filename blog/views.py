from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post

from .models import Post
# Create your views here.


# FBV
# def index(request):
#     posts = Post.objects.all().order_by('-pk')

#     return render(
#         request,
#         './blog/index.html',
#         {
#             'posts': posts,
#         }
#     )

# CBV

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'  # 내림차순으로 정렬해서 ListView해줘


def single_post_page(request, pk):
    post = Post.objects.all().get(pk=pk)

    return render(
        request,
        'blog/single_post_page.html',
        {
            'post': post
        }
    )
