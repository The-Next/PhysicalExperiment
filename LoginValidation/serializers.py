from LoginValidation.models import *
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('s_num',)

# 用于注册返回json数据
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','s_num','username','password')