from django.db import models

# Create your models here.


class HelloWorld(models.Model):

    # 아주 간단한 모델 작성
    text = models.CharField(max_length=255, null=False)