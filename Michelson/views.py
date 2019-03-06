from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from Michelson.utils import Michelsonmain
from Michelson.models import *
from Michelson.serializers import *
# Create your views here.
class MichelsonAPI(viewsets.ModelViewSet):
    '''
    retrieve:
            根据实验数据主键获得信息
    '''
    queryset = Michelson.objects.all().order_by('-pk')
    serializer_class = MichelsonSerializer
    permission_classes = (AllowAny,)  # 该接口权限为任意用户

    def create(self, request, *args, **kwargs):
        '''提交数据验证并保存'''
        data = request.data
        anwser = Michelsonmain.Michelson(data)
        serializer = MichelsonSerializer(data=anwser)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(anwser,HTTP_200_OK)
        return Response(serializer.error_messages,HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=['post'])
    def only_query(self, request, *args, **kwargs):#仅仅是计算数据，不保存数据库
        '''仅仅处理数据，不保存'''
        data = request.data
        anwser = Michelsonmain.Michelson(data)
        return Response(anwser, status=HTTP_200_OK)

    @action(detail=True,methods=['get'])
    def getListById(self,request, *args, **kwargs):
        '''根据用户的编号(非学号，用户的pk，不是实验的pk)获取其所有迈克尔逊干涉仪实验信息信息'''
        pk = kwargs['pk']
        serializer = MichelsonSerializer(Michelson.objects.filter(user_id__exact=pk),many=True)
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