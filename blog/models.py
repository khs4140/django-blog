from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    created_at = models.DateTimeField(
        auto_now=True)  # auto_now True 지정시 자동으로 설정됨
    updated_at = models.DateTimeField(
        auto_now=True)  # 글 작성시 아예 날짜/시간 정하는 것이 안나옴!

    # author 나중에 작ㅇ

    # admin -> Post 저장된 내용 확일할 수 있도록 __str__ 함수 생성
    # 어떻게 보여줄지 알려주는듯
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'
