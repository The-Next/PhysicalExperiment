# 用于序列化迈克尔逊干涉仪实验数据
from rest_framework import serializers
from Michelson.models import *

class MichelsonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Michelson
        fields = '__all__'