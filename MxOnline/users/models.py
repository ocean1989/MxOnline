from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):
    nick_name = models.CharField(max_length=50, verbose_name='昵称', default='')
    birday = models.DateField(verbose_name='生日', default='')
    gender = models.CharField(max_length=2, choices=(('male', '男'), ('female', '女')),default='女')
    address = models.CharField(max_length=100, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机', default='')
    image = models.ImageField(upload_to='image/%Y/%m', default='image/default.png', max_length=100)

    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
