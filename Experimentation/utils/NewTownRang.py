import json
import math
def newtown(dict={}):#,Instrumenttolerance,loss,lambdanew,uncertainty
    """左边读数，右边读数，仪器允差，半波损失，波长，波长不确定度"""
    '''d：环直径  rx_x：曲率半径 r：右边度数 l：左边读数 d_x：直径平方  xvaluey：两直径座差 uncertainty：不确定度 answer：测得曲率半径 lambda：波长nm'''
    dict['d30'] = round(dict['l30'] - dict['r30'],4)
    dict['d29'] = round(dict['l29'] - dict['r29'],4)
    dict['d28'] = round(dict['l28'] - dict['r28'],4)
    dict['d27'] = round(dict['l27'] - dict['r27'],4)
    dict['d26'] = round(dict['l26'] - dict['r26'],4)
    dict['d25'] = round(dict['l25'] - dict['r25'],4)
    dict['d10'] = round(dict['l10'] - dict['r10'],4)
    dict['d9'] = round(dict['l9'] - dict['r9'],4)
    dict['d8'] = round(dict['l8'] - dict['r8'],4)
    dict['d7'] = round(dict['l7'] - dict['r7'],4)
    dict['d6'] = round(dict['l6'] - dict['r6'],4)
    dict['d5'] = round(dict['l5'] - dict['r5'],4)

    dict['d_30'] = round(dict['d30'] ** 2,4)
    dict['d_29'] = round(dict['d29'] ** 2,4)
    dict['d_28'] = round(dict['d28'] ** 2,4)
    dict['d_27'] = round(dict['d27'] ** 2,4)
    dict['d_26'] = round(dict['d26'] ** 2,4)
    dict['d_25'] = round(dict['d25'] ** 2,4)
    dict['d_10'] = round(dict['d10'] ** 2,4)
    dict['d_9'] = round(dict['d9'] ** 2,4)
    dict['d_8'] = round(dict['d8'] ** 2,4)
    dict['d_7'] = round(dict['d7'] ** 2,4)
    dict['d_6'] = round(dict['d6'] ** 2,4)
    dict['d_5'] = round(dict['d5'] ** 2,4)

    dict['r30_10'] = Radius(dict['d30'], dict['d10'],'30','10',dict)
    dict['r29_9'] = Radius(dict['d29'], dict['d9'],'29','9',dict)
    dict['r28_8'] = Radius(dict['d28'], dict['d8'],'28','8',dict)
    dict['r27_7'] = Radius(dict['d27'], dict['d7'],'27','7',dict)
    dict['r26_6'] = Radius(dict['d26'], dict['d6'],'26','6',dict)
    dict['r25_5'] = Radius(dict['d25'], dict['d5'],'25','5',dict)




    count = dict['r30_10']+dict['r29_9']+dict['r28_8']+dict['r27_7']+dict['r26_6']+dict['r25_5']

    dict['anwser'] = round(count/6,4)
    dict['uncertainty'] = uncertainty(dict)
    return dict


def Radius(d1,d2,x,y,dict={}):#曲率半径
    r=d1**2-d2**2
    dict["value"+x+"_"+y] = round(r,4)
    r=r/(80*dict['lamda'])*1000#单位换算
    return round(r,4)

def uncertainty(dict={}):#计算不确定度
    avg = dict['value30_10']+dict['value29_9']+dict['value28_8']+dict['value27_7']+dict['value26_6']+dict['value25_5']
    avg = avg/6
    A1 = (dict['value30_10']-avg/6)**2#A类不确定度
    A2 = (dict['value29_9'] - avg / 6) ** 2
    A3 = (dict['value28_8'] - avg / 6) ** 2
    A4 = (dict['value27_7'] - avg / 6) ** 2
    A5 = (dict['value26_6'] - avg / 6) ** 2
    A6 = (dict['value25_5'] - avg / 6) ** 2
    sumA = A1+A2+A3+A4+A5+A6
    A = math.sqrt(sumA/30)
    B = dict['Instrumenttolerance']/math.sqrt(3)#B类不确定度
    return round(math.sqrt(A**2+B**2)/1000,3)