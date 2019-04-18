import os
import time
import uuid

import matplotlib
import matplotlib.pyplot as plt
plt.switch_backend('agg')#添加这一句不会出现线程错误具体原因不明
import numpy as np
import math
import json

from PhysicalExperiment import settings

myfont = matplotlib.font_manager.FontProperties(fname='static/FZHaiCKJW.TTF')


def ThermalConductivity(dict,flag,request):
    D = []
    for i in range(1,7):
        D.append(dict['D'+str(i)])
    dict['D'] = np.sum(D)/len(D)
    y=[]
    for i in range(1,41):
        if 'Tp_'+str(i) in dict:
         y.append(dict['Tp_'+str(i)])

    x = []#冷却速率时间间隔
    sum = 0#
    for i in range(1,len(y)+1):
        x.append(sum)
        sum = sum+dict['space1']
    #拟合加热图像方程

    times = []#加热速率时间间隔
    sum = 0
    for i in range(1,len(dict['add_Ta'])+1):
        times.append(sum)
        sum = sum+dict['space2']
    z_a = np.polyfit(times,dict['add_Ta'],2)#2次多项式拟合
    z_p = np.polyfit(times,dict['add_Tp'],  2)
    p_a = np.poly1d(z_a)#原方程
    p_p = np.poly1d(z_p)
    a_vals = p_a(times)
    p_vals = p_p(times)
    plt.plot(times, a_vals, 'r', label='Ta')
    plt.plot(times, p_vals, 'r', label='Tp')
    plt.xlabel('时间(S)', fontproperties=myfont,fontsize=18)
    plt.ylabel('温度(°C)', fontproperties=myfont,fontsize=18)
    plt.legend(loc=4)  # 指定legend的位置,可以自己help它的用法
    plt.title('散热盘加热曲线', fontproperties=myfont,fontsize=18)
    if flag:
        code = uuid.uuid1().__str__()

        ss = time.strftime("%Y/%m/%d", time.localtime())
        if not os.path.exists('media/'+ss+'/'):
            os.makedirs('media/'+ss+'/')
        dict['img1'] = 'media/'+ss+'/'+code+'.png'
        plt.savefig('media/'+ss+'/'+code+'.png')
    else:
        code = uuid.uuid1().__str__()
        plt.savefig('media/temp/'+code+'.png')
        dict['img1'] = request.scheme+'://'+request.META['HTTP_HOST']+'/media/temp/'+code+'.png'

    plt.close()





    #拟合散热盘图像与方程
    z1 = np.polyfit(x, y, 2)  # 用2次多项式拟合
    p1 = np.poly1d(z1)#原方程
    p2 = np.poly1d(z1).deriv()#导数
    p3 = np.polyval(p2, dict['Tp'])#代入值

    #此处操作，将生成的二次方程解析为可以被html正确展示的格式

    str_i = p1.__str__().strip()
    list_i = list(str_i)
    count = 0
    for i in list_i:
        if i=='x':
            list_i.insert(count+1,'<sup>2</sup>')
            break
        count = count+1
    dict['p1'] = ''.join(list_i).replace("2\n",'')
    dict['p2'] = p2.__str__().replace("\n",'')
    dict['t'] = round(p3.__float__(), 4)
    yvals = p1(x)  # 也可以使用yvals=np.polyval(z1,x)
    plot2 = plt.plot(x, yvals, 'r', label='polyfit values')
    plt.xlabel('时间(S)', fontproperties=myfont,fontsize=18)
    plt.ylabel('温度(°C)', fontproperties=myfont,fontsize=18)
    plt.legend(loc=4)  # 指定legend的位置,可以自己help它的用法
    plt.title('散热盘冷却曲线', fontproperties=myfont,fontsize=18)
    if flag:
        code = uuid.uuid1().__str__()

        ss = time.strftime("%Y/%m/%d", time.localtime())
        if not os.path.exists('media/'+ss+'/'):
            os.makedirs('media/'+ss+'/')
        dict['img2'] = 'media/'+ss+'/'+code+'.png'
        plt.savefig('media/'+ss+'/'+code+'.png')
    else:
        code = uuid.uuid1().__str__()
        plt.savefig('media/temp/'+code+'.png')
        dict['img2'] = request.scheme+'://'+request.META['HTTP_HOST']+'/media/temp/'+code+'.png'

    plt.close()
    calculate_avg(dict)
    onepart = (dict['D']+4*dict['hp'])/(dict['D']+2*dict['hp'])
    twopart = dict['hb']/(dict['Ta']-dict['Tp'])
    threepart = 1/(math.pi*pow(dict['D'],2))
    dict['k'] = 2 * dict['m'] * dict['c'] * abs(dict['t']) * onepart * twopart * threepart
    dict['k'] = round(dict['k'], 4)
    return dict

def calculate_avg(dict={}):
    dict['hb'] = round((dict['hb_1']+dict['hb_2']+dict['hb_3']+dict['hb_4']+dict['hb_5']+dict['hb_6'])/6)