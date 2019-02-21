# 用于序列化牛顿环实验数据
from rest_framework import serializers
from Experimentation.models import *

class NewtownSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewTown
        fields = '__all__'
