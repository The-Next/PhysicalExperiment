from django.http import FileResponse
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from ThermalConductivity.utils import ThermalConductivitymain,PDF
from ThermalConductivity.models import *
from ThermalConductivity.serializers import *
# Create your views here.
class ThermalConductivityAPI(viewsets.ModelViewSet):
    '''
    retrieve:
            根据实验数据主键获得信息
    '''
    queryset = ThermalConductivity.objects.all().order_by('-pk')
    serializer_class = ThermalConductivitySerializer
    permission_classes = (AllowAny,)  # 该接口权限为任意用户

    def create(self, request, *args, **kwargs):
        '''提交数据验证并保存'''
        data = request.data
        anwser = ThermalConductivitymain.ThermalConductivity(data,True,request)

        code = PDF.PDF(anwser)  # 制作pdf
        # del anwser['add_Ta']
        # del anwser['add_Tp']
        anwser['uu_id'] = code
        serializer = ThermalConductivitySerializer(data=anwser)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            ThermalConductivity_PDF.objects.create(user_name=anwser['user_name'],user_num=anwser['user_num'],uu_id=code,pdf_file='media/pdf/ThermalConductivity/'+code+'.pdf')#将pdf信息存入数据库
            anwser['img1'] = request.scheme+'://' + request.META['HTTP_HOST'] + "/" + anwser['img1']#手动拼装url
            anwser['img2'] = request.scheme+'://'+request.META['HTTP_HOST']+"/"+anwser['img2']
            return Response(anwser,HTTP_200_OK)
        return Response(serializer.error_messages,HTTP_400_BAD_REQUEST)




    @action(detail=False, methods=['post'])
    def only_query(self, request, *args, **kwargs):#仅仅是计算数据，不保存数据库
        '''仅仅处理数据，不保存'''
        data = request.data
        anwser = ThermalConductivitymain.ThermalConductivity(data,False,request)
        return Response(anwser, status=HTTP_200_OK)

    @action(detail=True,methods=['get'])
    def getListById(self,request, *args, **kwargs):
        '''根据用户的编号(非学号，用户的pk，不是实验的pk)获取其所有迈克尔逊干涉仪实验信息信息'''
        pk = kwargs['pk']
        serializer = ThermalConductivitySerializer(ThermalConductivity.objects.filter(user_id__exact=pk),many=True)
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

class ThermalConductivityAPI_PDF(viewsets.ModelViewSet):#pdf程序
    queryset = ThermalConductivity_PDF.objects.all().order_by('-pk')
    serializer_class = ThermalConductivity_PDFSerializer
    permission_classes = (AllowAny,)  # 该接口权限为任意用户
    @action(detail=False, methods=['post'])
    def get_pdf(self,request,*args,**kwargs):
        '''根据code获取对应对pdf文件,只需传入code值'''
        serializer_class = ThermalConductivity_PDF
        permission_classes = (AllowAny,)  # 该接口权限为任意用户
        data = request.data
        pdf = data['uu_id']
        filename = ThermalConductivity_PDF.objects.filter(uu_id=pdf).values('uu_id','pdf_file')
        file = open(filename[0]['pdf_file'],'rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="%s.pdf"' % (filename[0]['uu_id'])
        return response