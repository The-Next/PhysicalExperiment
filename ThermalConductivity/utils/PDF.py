import datetime
import uuid
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.pdfbase import pdfmetrics

from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.platypus import *
pdfmetrics.registerFont(UnicodeCIDFont('STSong-Light'))
import reportlab.lib.fonts
reportlab.lib.fonts.ps2tt = lambda psfn: ('STSong-Light', 0, 0)
reportlab.lib.fonts.tt2ps = lambda fn, b, i: 'STSong-Light'
from reportlab.lib.styles import ParagraphStyle

def PDF(dict={}):
    story = []
    reportlab.lib.styles.ParagraphStyle.defaults['wordWrap'] = 'CJK'
    stylesheet = getSampleStyleSheet()
    normalStyle = stylesheet['Normal']
    style = stylesheet['BodyText']
    style.fontName = 'STSong-Light'
    style.leading = 10#行距

    styleword = stylesheet['Normal']
    styleword.wordWrap = 'CJK'
    styleword.fontName = 'STSong-Light'
    styleword.leading = 10
    styleword.alignment = 1  # 居中
    ParagraphStyle.defaults['workWrap'] = "CJK"  # 中文自动换行


    #表格1
    data1 = [['n','1','2','3','4','5','6','7','8','9','10'],
            ['Ta (°C)',dict['add_Ta'][0],dict['add_Ta'][1],dict['add_Ta'][2],dict['add_Ta'][3],dict['add_Ta'][4],dict['add_Ta'][5],dict['add_Ta'][6],dict['add_Ta'][7],dict['add_Ta'][8],dict['add_Ta'][9]],
            ['Tp (°C)',dict['add_Tp'][0],dict['add_Tp'][1],dict['add_Tp'][2],dict['add_Tp'][3],dict['add_Tp'][4],dict['add_Tp'][5],dict['add_Tp'][6],dict['add_Tp'][7],dict['add_Tp'][8],dict['add_Tp'][9]],
            ['n', '10', '11', '12', '13', '14', '15', '16', '17', '18', '20'],
            ['Ta (°C)', dict['add_Ta'][10], dict['add_Ta'][11], dict['add_Ta'][12], dict['add_Ta'][13], dict['add_Ta'][14], dict['add_Ta'][15], dict['add_Ta'][16], dict['add_Ta'][17], dict['add_Ta'][18], dict['add_Ta'][19]],
            ['Tp (°C)', dict['add_Tp'][10], dict['add_Tp'][11], dict['add_Tp'][12], dict['add_Tp'][13], dict['add_Tp'][14], dict['add_Tp'][15], dict['add_Tp'][16], dict['add_Tp'][17], dict['add_Tp'][18], dict['add_Tp'][19]],
        ]

    style1 = [
        #('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'),  # 字体
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # 设置表格框线为黑色色，线宽为0.5
    ]

    table1 = Table(data1, colWidths=[70,36,36,36,36,36,36,36,36,36,36])
    table1.setStyle(TableStyle(style1))


    #表格2
    data2 = [['n','1','2','3','4','5','6','7','8','9','10'],
            ['Tp (°C)',dict['Tp_1'],dict['Tp_2'],dict['Tp_3'],dict['Tp_4'],dict['Tp_5'],dict['Tp_6'],dict['Tp_7'],dict['Tp_8'],dict['Tp_9'],dict['Tp_10']],
            ['n', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20'],
            ['Tp (°C)', dict['Tp_11'], dict['Tp_12'], dict['Tp_13'], dict['Tp_14'], dict['Tp_15'], dict['Tp_16'], dict['Tp_17'], dict['Tp_18'], dict['Tp_19'], dict['Tp_20']],
        ]

    style2 = [
        #('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'),  # 字体
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # 设置表格框线为黑色色，线宽为0.5
    ]
    table2 = Table(data2, colWidths=[70,36,36,36,36,36,36,36,36,36,36])
    table2.setStyle(TableStyle(style2))

    #表格3
    data3 = [['次数','1','2','3','4','5','6'],
            ['直径',dict['D1'],dict['D2'],dict['D3'],dict['D4'],dict['D5'],dict['D6']],
            ['厚度', dict['hb_1'], dict['hb_2'], dict['hb_3'], dict['hb_4'], dict['hb_5'], dict['hb_6']],
        ]

    style3 = [
        #('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'),  # 字体
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # 设置表格框线为黑色色，线宽为0.5
    ]
    table3 = Table(data3, colWidths=[90,55,55,55,55,55,55])
    table3.setStyle(TableStyle(style3))
    #图片
    K1 = Image(filename=dict['img1'])
    K1.drawHeight = 180
    K1.drawWidth = 200
    K2 = Image(filename=dict['img2'])
    K2.drawHeight = 180
    K2.drawWidth = 200

    styleimg = [
        #('ALIGN',(0,0),(-1,-1),'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'),  # 字体
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
    ]
    dataimg = [[
        K1,K2]
    ]
    tableimg = Table(dataimg, colWidths=[230,230])
    tableimg.setStyle(TableStyle(styleimg))
    #字
    P = Paragraph('<b>加热盘Ta和散热盘Tp的温度（稳态法）</b>',style)
    P1 = Paragraph('散热盘初温10°C加热盘初温10°C，加热热时间间隔'+str(dict['space2'])+'s',style)
    PL = Paragraph('',style)
    I = Paragraph('<b>散热盘Tp的冷却速率的测量（加热热时间间隔'+str(dict['space1'])+'s）</b>',style)
    H = Paragraph('<b>橡胶盘几何参数测量（橡胶盘质量'+str(dict['m'])+'kg，橡胶盘比热容'+str(dict['c'])+'J/(kg*K)）</b>',style)
    #K =Paragraph('<img src="f3.png" height=180 width=200 valign="middle" /><img src="f4.png" height=180 width=200 valign="middle"/>',style)
    #K.hAlign='center'
    #K.vAlign = "center"

    #主面板
    rpt_title = '<para autoLeading="off" fontSize=16 align=center><b><font face="STSong-Light">郑州轻工业大学物理实验报告</font></b><br/><br/><br/></para>'
    component_data = [['学生姓名',dict['user_name'],'学号',dict['user_num'],'学院','软件学院'],
                      ['专业班级','软件工程17-03','时间','%s.%s.%s'%(datetime.datetime.now().year,datetime.datetime.now().month,datetime.datetime.now().day),'教师',''],
                      ['实验名称','稳态法测量非良导体热导率实验','','','',''],
                      [[tableimg,P,PL,table1,I,PL,table1,H,PL,table3],'','','','',''],
                      ]

    stylex = [
        #('ALIGN',(0,0),(-1,-1),'CENTER'),

        ('FONTNAME', (0, 0), (-1, -1), 'STSong-Light'),  # 字体
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.black),  # 设置表格内文字颜色
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black),  # 设置表格框线为黑色色，线宽为0.5
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('SPAN', (1, 2), (5, 2)),
        ('SPAN', (0, 3), (5, 3)),
        ('SPAN', (0,4), (2, 4)),
        ('SPAN', (3,4), (5, 4)),
        #('ALIGN',(0,3),(-1,-1),'CENTER'),
    ]

    component_table = Table(component_data, colWidths=[50,100,50,100,50,100])
    component_table.setStyle(TableStyle(stylex))
    story.append(Paragraph(rpt_title,normalStyle))
    story.append(component_table)
    code = uuid.uuid1().__str__()#生成唯一标识符
    sss = reportlab.platypus.SimpleDocTemplate('media/pdf/ThermalConductivity'+code+'.pdf')
    sss.build(story)
    return code