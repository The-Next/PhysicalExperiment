import json
import math
def newtown(dict={}):#,Instrumenttolerance,loss,lambdanew,uncertainty
    """左边读数，右边读数，仪器允差，半波损失，波长，波长不确定度"""
    '''d：环直径  rx_x：曲率半径 r：右边度数 l：左边读数 d_x：直径平方  xvaluey：两直径座差 uncertainty：不确定度 answer：测得曲率半径 lambda：波长nm'''
    dict['d35'] = round(dict['l35'] - dict['r35'],4)
    dict['d34'] = round(dict['l34'] - dict['r34'],4)
    dict['d33'] = round(dict['l33'] - dict['r33'],4)
    dict['d32'] = round(dict['l32'] - dict['r32'],4)
    dict['d31'] = round(dict['l31'] - dict['r31'],4)
    dict['d30'] = round(dict['l30'] - dict['r30'],4)
    dict['d15'] = round(dict['l15'] - dict['r15'],4)
    dict['d14'] = round(dict['l14'] - dict['r14'],4)
    dict['d13'] = round(dict['l13'] - dict['r13'],4)
    dict['d12'] = round(dict['l12'] - dict['r12'],4)
    dict['d11'] = round(dict['l11'] - dict['r11'],4)
    dict['d10'] = round(dict['l10'] - dict['r10'],4)

    dict['d_35'] = round(dict['d35'] ** 2,4)
    dict['d_34'] = round(dict['d34'] ** 2,4)
    dict['d_33'] = round(dict['d33'] ** 2,4)
    dict['d_32'] = round(dict['d32'] ** 2,4)
    dict['d_31'] = round(dict['d31'] ** 2,4)
    dict['d_30'] = round(dict['d30'] ** 2,4)
    dict['d_15'] = round(dict['d15'] ** 2,4)
    dict['d_14'] = round(dict['d14'] ** 2,4)
    dict['d_13'] = round(dict['d13'] ** 2,4)
    dict['d_12'] = round(dict['d12'] ** 2,4)
    dict['d_11'] = round(dict['d11'] ** 2,4)
    dict['d_10'] = round(dict['d10'] ** 2,4)

    dict['r35_15'] = Radius(dict['d35'], dict['d15'],'35','15',dict)
    dict['r34_14'] = Radius(dict['d34'], dict['d14'],'34','14',dict)
    dict['r33_13'] = Radius(dict['d33'], dict['d13'],'33','13',dict)
    dict['r32_12'] = Radius(dict['d32'], dict['d12'],'32','12',dict)
    dict['r31_11'] = Radius(dict['d31'], dict['d11'],'31','11',dict)
    dict['r30_10'] = Radius(dict['d30'], dict['d10'],'30','10',dict)




    count = dict['r35_15']+dict['r34_14']+dict['r33_13']+dict['r32_12']+dict['r31_11']+dict['r30_10']

    dict['anwser'] = round(count/6,4)
    dict['uncertainty'] = uncertainty(dict)
    return dict


def Radius(d1,d2,x,y,dict={}):#曲率半径
    r=d1**2-d2**2
    dict["value"+x+"_"+y] = round(r,4)
    r=r/(80*dict['lamda'])*1000#单位换算
    return round(r,4)

def uncertainty(dict={}):#计算不确定度
    avg = dict['value35_15']+dict['value34_14']+dict['value33_13']+dict['value32_12']+dict['value31_11']+dict['value30_10']
    avg = avg/6
    A1 = (dict['value35_15']-avg/6)**2#A类不确定度
    A2 = (dict['value34_14'] - avg / 6) ** 2
    A3 = (dict['value33_13'] - avg / 6) ** 2
    A4 = (dict['value32_12'] - avg / 6) ** 2
    A5 = (dict['value31_11'] - avg / 6) ** 2
    A6 = (dict['value30_10'] - avg / 6) ** 2
    sumA = A1+A2+A3+A4+A5+A6
    A = math.sqrt(sumA/30)
    B = dict['Instrumenttolerance']/math.sqrt(3)#B类不确定度
    return round(math.sqrt(A**2+B**2)/1000,3)