from django.shortcuts import render
from django.views.generic import ListView, DetailView

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

# CBV로 포스트 목록 구현

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'  # 내림차순으로 정렬해서 ListView해줘


# def single_post_page(request, pk):
#     post = Post.objects.all().get(pk=pk)

#     return render(
#         request,
#         'blog/single_post_page.html',
#         {
#             'post': post
#         }
#     )

# CBV 방식으로 포스트 상세페이지 구현
class PostDetail(DetailView):
    model = Post
    # 이거 안바꾸고 그냥 파일 이름을 post_detail.html로 수정하면 가능
    template_name = 'blog/single_post_page.html'
