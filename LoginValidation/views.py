from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from django.shortcuts import render
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import *
from django.contrib.auth.hashers import make_password
from LoginValidation.models import *
from LoginValidation.serializers import *
from rest_framework.views import APIView
# Create your views here.
#用于用户注册
class UserRegisterAPIView(APIView):
    queryset = User
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)#该接口权限为任意用户

    def post(self ,request, format=None):
        data = request.data.copy()
        s_num = data.get('s_num')
        data['password'] = make_password(data.get('password'))
        if User.objects.filter(s_num__exact=s_num):#如果用户名存在，返回错误
            return Response("学号已存在",HTTP_400_BAD_REQUEST)
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid(raise_exception=True):#验证表单，如果错误会返回404
            serializer.save()
            return Response(serializer.data,status=HTTP_200_OK)
        return Response(serializer.error_messages,status=HTTP_400_BAD_REQUEST)

class CustomBackend(ModelBackend):
    '''
    自定义用户验证规则
    '''
    def authenticate(self, request, username=None, password=None, **kwargs):
        print(12)
        try:
            user = User.objects.get(Q(username=username) | Q(s_num=username))
            print(user.username)
            if user.check_password(password):
                return user
        except Exception as e:
            return None