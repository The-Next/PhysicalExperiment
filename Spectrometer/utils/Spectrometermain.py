import json
import math


def Spectrometer(phi={}):#分光计自准法
    phi['phi1'] = supplement(phi['phi1_1'], phi['phi2_1'], phi['phi3_1'], phi['phi4_1'])
    phi['phi2'] = supplement(phi['phi1_2'], phi['phi2_2'], phi['phi3_2'], phi['phi4_2'])
    phi['phi3'] = supplement(phi['phi1_3'], phi['phi2_3'], phi['phi3_3'], phi['phi4_3'])
    phi['phi4'] = supplement(phi['phi1_4'], phi['phi2_4'], phi['phi3_4'], phi['phi4_4'])
    phi['phi5'] = supplement(phi['phi1_5'], phi['phi2_5'], phi['phi3_5'], phi['phi4_5'])
    phi['phi6'] = supplement(phi['phi1_6'], phi['phi2_6'], phi['phi3_6'], phi['phi4_6'])
    phi['phiba'] = avg([phi['phi1'],phi['phi2'],phi['phi3'],phi['phi4'],phi['phi5'],phi['phi6']])
    phi['delta'] = uncertainty(phi)
    phi['alpha'] = alpha(phi['phiba'])
    return phi

def uncertainty(phi={}):#不确定度计算
    p1 = anglesquare(anglesub(phi['phi1'],phi['phiba']))
    p2 = anglesquare(anglesub(phi['phi2'], phi['phiba']))
    p3 = anglesquare(anglesub(phi['phi3'], phi['phiba']))
    p4 = anglesquare(anglesub(phi['phi4'], phi['phiba']))
    p5 = anglesquare(anglesub(phi['phi5'], phi['phiba']))
    p6 = anglesquare(anglesub(phi['phi6'], phi['phiba']))

    sum = p1+p2+p3+p4+p5+p6
    uncertaintyA = math.sqrt(sum/(5*6))#A类不确定度
    uncertaintyB = math.radians(1/60)/math.sqrt(3)#B类不确定度
    p = math.sqrt(uncertaintyA**2+uncertaintyB**2)#由弧度转化为分度
    p = math.degrees(p)
    return str(round(p,4))+"°"


def anglesquare(line):#角度的平方计算
    du_1 = line.find("°")
    du1 = line[:du_1]
    fen1 = line[du_1 + 1:]

    du = int(du1)
    fen = int(fen1)
    du = du+fen/60

    rad = math.radians(du)#将度转化为弧度计算
    rad = rad ** 2
    return rad


def alpha(phiba):#计算alpha角
    return anglesub('180°0',phiba)
def avg(array=[]):
    fensum = 0
    dusum = 0
    count = 0
    for i in array:
        # 以°为界限，截取前后部分
        du_1 = i.find("°")
        du = i[:du_1]
        fen = i[du_1 + 1:]
        fensum = fensum+int(fen)
        dusum = dusum+int(du)
        count = count+1
    fenba = fensum/count
    duba = dusum/count
    divdu = duba%1#获取小数位
    divdu = divdu*60#化为分数位
    fenba = fenba+divdu#将度位的小数位放在分位
    if fenba>=60:#分位满60进一
        fen = fen - 60
        du = du+1
    line = str(math.floor(duba))+"°"+str(round(fenba))#重新组装,度位舍弃小数位，分位四舍五入
    return line



def supplement(phi1,phi2,phi_1,phi_2):# 计算补角

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