import math
import json
def Michelson(dict={}):
    difference=[]#储存差值，用于d的不确定度计算
    dict['deltad']=round(dertaD(dict),5)#△d平均值
    difference.append(abs(dict['seven'] - dict['one']))
    difference.append(abs(dict['eight'] - dict['two']))
    difference.append(abs(dict['nine'] - dict['three']))
    difference.append(abs(dict['ten'] - dict['four']))
    difference.append(abs(dict['eleven'] - dict['five']))
    difference.append(abs(dict['twelfth'] - dict['six']))
    dict['seven_one'] = round(abs(dict['seven'] - dict['one']),5)#取绝对值并保留五位小数
    dict['eight_two'] = round(abs(dict['seven'] - dict['one']),5)
    dict['nine_three'] = round(abs(dict['seven'] - dict['one']),5)
    dict['ten_four'] = round(abs(dict['seven'] - dict['one']),5)
    dict['eleven_five'] = round(abs(dict['seven'] - dict['one']),5)
    dict['twelfth_six'] = round(abs(dict['seven'] - dict['one']),5)
    dict['deltadD'] = round(dertaDD(dict['deltad'],difference,dict),5)#△(△d)  d的不确定度
    dict['lambda_avg'] = 0
    for i in difference:#求lambda的平均值
        dict['lambda_avg'] = dict['lambda_avg'] + lamda(i)
    dict['lambda_avg'] = round(dict['lambda_avg'] / 6,5)
    dict['deltadlambda'] = round(2*dict['deltadD']*1000000/300,5)#lambda不确定度
    dict['E'] = abs(dict['lambda_avg'] - 632.8) / 632.8  # 相对不确定度
    dict['E'] = str(round(dict['E'] * 100,2)) + '%'#将分数化为百分数字符串
    return dict



def dertaD(dict={}):#计算△d
    avge=0
    avge=abs(dict['seven']-dict['one'])+abs(dict['eight']-dict['two'])+abs(dict['nine']-dict['three'])+abs(dict['ten']-dict['four'])+abs(dict['eleven']-dict['five'])+abs(dict['twelfth']-dict['six'])
    return avge/6

def dertaDD(d,list=[],dict={}):#d的不确定度
    count=0
    for l in list:
        count=count+abs(l-d)**2
    d = math.sqrt(count/(5*6))
    return math.sqrt(d**2+dict['Instrumenttolerance']**2)

def lamda(d):#计算lambda的值
    return 2*d*1000000/300