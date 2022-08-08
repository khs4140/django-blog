from distutils.command.upload import upload
from django.db import models
import os
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    # 이미지 업로드 blank는 Null 허용
    head_image = models.ImageField(
        upload_to='blog/images/%Y/%m/%d', blank=True)

    # 파일 업로드!
    # post.file_upload = 파일 이름
    # post.file_upload.url = 파일 있는 경로
    file_upload = models.FileField(
        upload_to='blog/files/%Y/%m/%d', blank=True
    )

    created_at = models.DateTimeField(
        auto_now=True)  # auto_now True 지정시 자동으로 설정됨
    updated_at = models.DateTimeField(
        auto_now=True)  # 글 작성시 아예 날짜/시간 정하는 것이 안나옴!

    # author 나중에 작업

    # admin -> Post 저장된 내용 확일할 수 있도록 __str__ 함수 생성
    # 어떻게 보여줄지 알려주는듯
    def __str__(self):
        return f'[{self.pk}] {self.title}'

    def get_absolute_url(self):
        return f'/blog/{self.pk}'

    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]
