from django.contrib.auth.models import *

from django.db import models
# Create your models here.
class User(AbstractUser):
    s_num = models.CharField(max_length=20,default='',blank=True,verbose_name='学号')#加限制，不能重复