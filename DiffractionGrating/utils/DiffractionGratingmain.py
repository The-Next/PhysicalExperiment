import json
import math
'''
Beyond_yellow黄外光衍射角  Beyond_yellow1等 测量值 Beyond_yellow_k级次
Inside_yellow黄内光衍射角  Inside_yellow1等 测量值 Inside_yellow_k级次
green  绿光衍射角 green1等 测量值 green_k级次
blue 蓝光衍射角 blue1等 测量值 blue_k级次
d 光栅常数
x_D角色散率
'''
def diffraction_grating(dict):
    Beyond_yellow = supplement(dict['Beyond_yellow1'], dict['Beyond_yellow2'], dict['Beyond_yellow3'], dict['Beyond_yellow4'])
    Inside_yellow = supplement(dict['Inside_yellow1'], dict['Inside_yellow2'],dict['Inside_yellow3'],dict['Inside_yellow4'])
    green = supplement(dict['green1'],dict['green2'],dict['green3'],dict['green4'])
    blue = supplement(dict['blue1'], dict['blue2'], dict['blue3'], dict['blue4'])
    dict['Beyond_yellow'] = anglediv(Beyond_yellow,"0°0")
    dict['Inside_yellow'] = anglediv(Inside_yellow,"0°0")
    dict['green'] = anglediv(green,"0°0")
    dict['blue'] = anglediv(blue,"0°0")

    dict['Beyond_yellow_lambda'] = lamda(dict['d'],dict['Beyond_yellow_k'],dict['Beyond_yellow'])
    dict['Inside_yellow_lambda'] = lamda(dict['d'], dict['Inside_yellow_k'], dict['Inside_yellow'])
    dict['green_lambda'] = lamda(dict['d'], dict['green_k'], dict['green'])
    dict['blue_lambda'] = lamda(dict['d'], dict['blue_k'], dict['blue'])

    dict['Beyond_yellow_D'] = dispersive_power(dict['d'],dict['Beyond_yellow_k'],dict['Beyond_yellow'])
    dict['Inside_yellow_D'] = dispersive_power(dict['d'], dict['Inside_yellow_k'], dict['Inside_yellow'])
    dict['green_D'] = dispersive_power(dict['d'], dict['green_k'], dict['green'])
    dict['blue_D'] = dispersive_power(dict['d'], dict['blue_k'], dict['blue'])

    dict['Beyond_yellow_R'] = get_R(dict['Beyond_yellow_k'],dict['N'])
    dict['Inside_yellow_R'] = get_R(dict['Inside_yellow_k'], dict['N'])
    dict['green_R'] = get_R(dict['green_k'], dict['N'])
    dict['blue_R'] = get_R(dict['blue_k'], dict['N'])

    dict['Beyond_yellow_delta_lambda'] = get_delta_lambda(dict['Beyond_yellow_R'],dict['Beyond_yellow_lambda'])
    dict['Inside_yellow_delta_lambda'] = get_delta_lambda(dict['Inside_yellow_R'], dict['Inside_yellow_lambda'])
    dict['green_delta_lambda'] = get_delta_lambda(dict['green_R'], dict['green_lambda'])
    dict['blue_delta_lambda'] = get_delta_lambda(dict['blue_R'], dict['blue_lambda'])


    return dict

def get_delta_lambda(R,lamba):#计算波长差
    return round(lamba/R,4)


def get_R(k,N):#计算分辨本领
    return k*N

def dispersive_power(d,k,phi):#计算角色散率
    du_1 = phi.find("°")
    du1 = phi[:du_1]
    fen1 = phi[du_1 + 1:]

    du = int(du1)
    fen = int(fen1)
    du = du + fen / 60
    rad = math.radians(du)  # 将度转化为弧度计算

    return round(k/(d*math.cos(rad)),7)

def lamda(d,k,phi):#求波长
    du_1 = phi.find("°")
    du1 = phi[:du_1]
    fen1 = phi[du_1 + 1:]

    du = int(du1)
    fen = int(fen1)
    du = du+fen/60
    rad = math.radians(du)#将度转化为弧度计算

    return round(d*math.sin(rad)/k,3)

def supplement(phi1,phi2,phi_1,phi_2):# 计算衍射角

    phia=anglesub(phi1,phi2)
    phib=anglesub(phi_1,phi_2)
    phi=anglediv(phib,phia)
    return phi



def anglesub(line1,line2):#角度相减
    #以°为界限，截取前后部分
    du_1=line1.find("°")
    du1=line1[:du_1]
    fen1=line1[du_1+1:]

    du_2=line2.find("°")
    du2=line2[:du_2]
    fen2=line2[du_2+1:]

    if int(du2)>int(du1):
        du = int(du2)-int(du1)#度数部分相减
        fen = int(fen2) - int(fen1)#分部分相减
        if fen<0:#60进制减法运算
            fen = 60+fen
            du = du-1
    elif int(du2)<int(du1):
        du = int(du1) - int(du2)  # 度数部分相减
        fen = int(fen1) - int(fen2)  # 分部分相减
        if fen < 0:  # 60进制减法运算
            fen = 60 + fen
            du = du - 1
    else:
        du=0
        fen = abs(int(fen2) - int(fen1))

    line = str(du)+"°"+str(fen)#重新组装
    return line

def angleadd(line1,line2):#角度相加
    #以°为界限，截取前后部分
    du_1=line1.find("°")
    du1=line1[:du_1]
    fen1=line1[du_1+1:]

    du_2=line2.find("°")
    du2=line2[:du_2]
    fen2=line2[du_2+1:]

    du = int(du2)+int(du1)#度数部分相加

    fen = int(fen2) + int(fen1)#分部分相加
    if fen>=60:#60进制加法运算
        fen = fen-60
    du = du + 1

    line = str(du)+"°"+str(fen)#重新组装
    return line

def anglediv(line1,line2):#两个角度取平均值
    # 以°为界限，截取前后部分
    du_1 = line1.find("°")
    du1 = line1[:du_1]
    fen1 = line1[du_1 + 1:]

    du_2 = line2.find("°")
    du2 = line2[:du_2]
    fen2 = line2[du_2 + 1:]

    du = (int(du2) + int(du1))/2  # 度数部分取平均
    divdu = du%1#获取小数位
    divdu = divdu*60#化为分数位

    fen = (int(fen2) + int(fen1))/2#分数位取平均
    fen = fen+divdu#将度位的小数位放在分位
    if fen>=60:#分位满60进一
        fen = fen - 60
        du = du+1
    line = str(math.floor(du))+"°"+str(round(fen))#重新组装,度位舍弃小数位，分位四舍五入
    return line