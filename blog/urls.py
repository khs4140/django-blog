from django.urls import URLPattern, path
from . import views

urlpatterns = [

    path('', views.PostList.as_view()),  # CBV 방식의 포스트 목록 구현 (Index 대체)
    # CBV 방식의 상세페이지 구현 (single_post_page 대체)
    path('<int:pk>', views.PostDetail.as_view())
    # path('<int:pk>', views.single_post_page), # FBV 방식의 상세페이지 함수
    # path('', views.index), # FBV 방식의 index함수
]
