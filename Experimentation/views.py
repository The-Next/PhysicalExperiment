from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ViewSet

from Experimentation.utils import NewTownRang
import json
from Experimentation.models import *
from Experimentation.serializers import *
# Create your views here.
from rest_framework.views import APIView

#
class NewtownAPI(viewsets.ModelViewSet):#针对于提交数据和查询自己的数据
    '''
    retrieve:
            根据实验数据主键获得信息
    '''
    queryset = NewTown.objects.all().order_by('-pk')
    serializer_class = NewtownSerializer
    permission_classes = (AllowAny,)  # 该接口权限为任意用户

    def create(self, request, *args, **kwargs):#如果对面传过来的json串没有值的话，将会被作为字典解析，如果有值的话，会被作为json解析
        '''提交数据验证并保存'''
        data = request.data
        anwser = NewTownRang.newtown(data)
        serializer = NewtownSerializer(data=anwser)
        if serializer.is_valid(raise_exception=True):#验证表单，如果错误会返回404
            serializer.save()
            return Response(anwser,status=HTTP_200_OK)
        return Response(serializer.error_messages,status=HTTP_400_BAD_REQUEST)

       # return Response(anwser, status=HTTP_200_OK)
    @action(detail=False, methods=['post'])
    def only_query(self, request, *args, **kwargs):#仅仅是计算数据，不保存数据库
        '''仅仅处理数据，不保存'''
        data = request.data
        anwser = NewTownRang.newtown(data)
        return Response(anwser, status=HTTP_200_OK)

    @action(detail=True,methods=['get'])
    def getListById(self,request, *args, **kwargs):
        '''根据用户的编号(非学号，用户的pk，不是实验的pk)获取其所有牛顿环实验信息信息'''
        pk = kwargs['pk']
        serializer = NewtownSerializer(NewTown.objects.filter(user_id__exact=pk),many=True)
        data = serializer.data
        print(data)
        return Response(data,status=HTTP_200_OK)

    def list(self, request, *args, **kwargs):
        '''获取所有实验信息(当前没有需求，此接口无效，禁用)'''
        return Response('该接口不允许调用',HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        '''根据id删除数据(当前没有需求，此接口无效，禁用)'''
        return Response('该接口不允许调用',HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        '''根据主键更新信息，(当前没有需求，此接口无效，禁用)'''
        return Response("该接口不允许调用",HTTP_400_BAD_REQUEST)

    def partial_update(self, request, *args, **kwargs):
        '''根据主键更新部分信息，(当前没有需求，此接口无效，禁用)'''
        return Response("该接口不与许调用",HTTP_400_BAD_REQUEST)







    '''@action(detail=True, methods=['get'])#detail参数，可以设定是否需要主键
    def get_pk(self, request, *args, **kwargs):
        pk = kwargs['pk']  # 超级大坑，django用多参数列表接收参数
        serializer = NewtownSerializer(NewTown.objects.filter(id=pk), many=True)  # 第二个参数必带
        data = serializer.data
        return Response(data, status=HTTP_200_OK)'''




