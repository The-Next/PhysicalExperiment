import json
import math
def StaticYoungmodulus(dict={}):
    #计算增荷时与减荷时的平均值
    dict['n0_avg'] = round((dict['n0'] + dict['n_0'])/2,3)
    dict['n1_avg'] = round((dict['n1'] + dict['n_1'])/2,3)
    dict['n2_avg'] = round((dict['n2'] + dict['n_2'])/2,3)
    dict['n3_avg'] = round((dict['n3'] + dict['n_3'])/2,3)
    dict['n4_avg'] = round((dict['n4'] + dict['n_4'])/2,3)
    dict['n5_avg'] = round((dict['n5'] + dict['n_5'])/2,3)
    dict['n6_avg'] = round((dict['n6'] + dict['n_6'])/2,3)
    dict['n7_avg'] = round((dict['n7'] + dict['n_7'])/2,3)
    #逐差法计算增加四个砝码铁丝拉伸量△l的光杆放大量
    dict['n4_0'] = round((dict['n4_avg'] - dict['n0_avg'])/4,3)
    dict['n5_1'] = round((dict['n5_avg'] - dict['n1_avg'])/4,3)
    dict['n6_2'] = round((dict['n6_avg'] - dict['n2_avg'])/4,3)
    dict['n7_3'] = round((dict['n7_avg'] - dict['n3_avg'])/4,3)
    dict['ln'] = round((dict['n4_0']+dict['n5_1']+dict['n6_2']+dict['n7_3'])/4,3)

    F=1*9.8*4
    #直径
    dict['d_avg'] = round((dict['d1']+dict['d2']+dict['d3']+dict['d4']+dict['d5']+dict['d6'])/6,3)
    #结果E
    dict['E'] = (8*F*dict['L']+dict['D'])/(3.14*(dict['d_avg']**2)*dict['K']*dict['ln'])
    dict['E'] = round(dict['E']*10e9,3)

    dict['delta_dn'] = round(uncertainty_d(dict),3)
    dict['delta_ln'] = round(uncertainty_l(dict),3)
    e=(0.03/F)**2+(dict['delta_L']/dict['L'])**2+(dict['delta_D']/dict['D'])**2+2*(dict['delta_dn']/dict['d_avg'])**2+(dict['delta_ln']/dict['ln'])**2+(dict['delta_K']/dict['K'])**2
    dict['relative_E'] = math.sqrt(e)#相对不确定度
    dict['delta_E'] = round(dict['relative_E']*dict['E'],3)#E的不确定度
    dict['relative_E'] = str(round(dict['relative_E'] * 100,2)) + '%'#将分数化为百分数字符串
    return dict


def uncertainty_d(dict={}):#计算d的不确定度
    n_1 = (dict['d_avg']-dict['d1'])**2
    n_2 = (dict['d_avg']-dict['d2'])**2
    n_3 = (dict['d_avg']-dict['d3'])**2
    n_4 = (dict['d_avg']-dict['d4'])**2
    n_5 = (dict['d_avg']-dict['d5'])**2
    n_6 = (dict['d_avg']-dict['d6'])**2

    sum = n_1+n_2+n_3+n_4+n_5+n_6
    A = math.sqrt(sum/30)#A类不确定度
    B = dict['micrometer']/math.sqrt(3)#B类不确定度，micrometer为螺旋测微器的允差
    return math.sqrt((A**2)+(B**2))#合成不确定度



def uncertainty_l(dict={}):#计算l的不确定度
    l_1 = (dict['ln']-dict['n4_0'])**2
    l_2 = (dict['ln']-dict['n5_1'])**2
    l_3 = (dict['ln']-dict['n6_2'])**2
    l_4 = (dict['ln']-dict['n7_3'])**2

    sum = l_1+l_2+l_3+l_4
    A = math.sqrt(sum/12)#A类不确定度
    B = dict['verniercaliper'] / math.sqrt(3)#B类不确定度，verniercaliper为游标卡尺允差
    return math.sqrt((A ** 2) + (B ** 2))  # 合成不确定度