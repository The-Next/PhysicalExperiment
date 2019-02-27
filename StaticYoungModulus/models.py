from django.db import models

# Create your models here.
class StaticYooungModulus(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号', blank=True, null=True)
    user_name = models.CharField(verbose_name='学生姓名', max_length=20, blank=True, null=True, default='李华')
    user_num = models.CharField(verbose_name='学生学号', max_length=20, blank=True, null=True, default='1')
    #测量值，增荷值
    n0 = models.DecimalField(verbose_name='增荷值0', max_digits=15, decimal_places=5)
    n1 = models.DecimalField(verbose_name='增荷值1', max_digits=15, decimal_places=5)
    n2 = models.DecimalField(verbose_name='增荷值2', max_digits=15, decimal_places=5)
    n3 = models.DecimalField(verbose_name='增荷值3', max_digits=15, decimal_places=5)
    n4 = models.DecimalField(verbose_name='增荷值4', max_digits=15, decimal_places=5)
    n5 = models.DecimalField(verbose_name='增荷值5', max_digits=15, decimal_places=5)
    n6 = models.DecimalField(verbose_name='增荷值6', max_digits=15, decimal_places=5)
    n7 = models.DecimalField(verbose_name='增荷值7', max_digits=15, decimal_places=5)
    #测量值，减荷值
    n_0 = models.DecimalField(verbose_name='减荷值0', max_digits=15, decimal_places=5)
    n_1 = models.DecimalField(verbose_name='减荷值1', max_digits=15, decimal_places=5)
    n_2 = models.DecimalField(verbose_name='减荷值2', max_digits=15, decimal_places=5)
    n_3 = models.DecimalField(verbose_name='减荷值3', max_digits=15, decimal_places=5)
    n_4 = models.DecimalField(verbose_name='减荷值4', max_digits=15, decimal_places=5)
    n_5 = models.DecimalField(verbose_name='减荷值5', max_digits=15, decimal_places=5)
    n_6 = models.DecimalField(verbose_name='减荷值6', max_digits=15, decimal_places=5)
    n_7 = models.DecimalField(verbose_name='减荷值7', max_digits=15, decimal_places=5)
    #测量值，直径
    d1 = models.DecimalField(verbose_name='直径1', max_digits=15, decimal_places=5)
    d2 = models.DecimalField(verbose_name='直径2', max_digits=15, decimal_places=5)
    d3 = models.DecimalField(verbose_name='直径3', max_digits=15, decimal_places=5)
    d4 = models.DecimalField(verbose_name='直径4', max_digits=15, decimal_places=5)
    d5 = models.DecimalField(verbose_name='直径5', max_digits=15, decimal_places=5)
    d6 = models.DecimalField(verbose_name='直径6', max_digits=15, decimal_places=5)
    d_avg = models.DecimalField(verbose_name='平均直径', max_digits=15, decimal_places=5)
    #输入参数
    L = models.DecimalField(verbose_name='金属丝原长', max_digits=15, decimal_places=5)
    D = models.DecimalField(verbose_name='光杆与望远镜镜尺距离', max_digits=15, decimal_places=5)
    K = models.DecimalField(verbose_name='光光杆常数', max_digits=15, decimal_places=5)
    delta_L = models.DecimalField(verbose_name='金属丝原长不确定度', max_digits=15, decimal_places=5)
    delta_D = models.DecimalField(verbose_name='光杆与望远镜镜尺距离不确定度', max_digits=15, decimal_places=5)
    delta_K = models.DecimalField(verbose_name='光光杆常数不确定度', max_digits=15, decimal_places=5)
    micrometer = models.DecimalField(verbose_name='螺旋测微器允差', max_digits=15, decimal_places=5)
    verniercaliper = models.DecimalField(verbose_name='游标卡尺允差', max_digits=15,decimal_places=5)
    #增荷时与减荷时的平均值
    n0_avg = models.DecimalField(verbose_name='差值0', max_digits=15, decimal_places=5)
    n1_avg = models.DecimalField(verbose_name='差值1', max_digits=15, decimal_places=5)
    n2_avg = models.DecimalField(verbose_name='差值2', max_digits=15, decimal_places=5)
    n3_avg = models.DecimalField(verbose_name='差值3', max_digits=15, decimal_places=5)
    n4_avg = models.DecimalField(verbose_name='差值4', max_digits=15, decimal_places=5)
    n5_avg = models.DecimalField(verbose_name='差值5', max_digits=15, decimal_places=5)
    n6_avg = models.DecimalField(verbose_name='差值6', max_digits=15, decimal_places=5)
    n7_avg = models.DecimalField(verbose_name='差值7', max_digits=15, decimal_places=5)
    #逐差法计算过程
    n4_0 = models.DecimalField(verbose_name='4与0座差', max_digits=15, decimal_places=5)
    n5_1 = models.DecimalField(verbose_name='5与1座差', max_digits=15, decimal_places=5)
    n6_2 = models.DecimalField(verbose_name='6与2座差', max_digits=15, decimal_places=5)
    n7_3 = models.DecimalField(verbose_name='7与3座差', max_digits=15, decimal_places=5)
    #四个砝码铁丝拉伸量△l的光杆放大量
    ln = models.DecimalField(verbose_name='四个砝码铁丝拉伸量△l的光杆放大量', max_digits=15, decimal_places=5)
    #计算出来的不确定度
    delta_dn = models.DecimalField(verbose_name= 'd的不确定度', max_digits=15, decimal_places=5)
    delta_ln = models.DecimalField(verbose_name= 'l的不确定度', max_digits=15, decimal_places=5)
    E = models.DecimalField(verbose_name='杨氏模量', max_digits=15, decimal_places=5)
    delta_E = models.DecimalField(verbose_name='不确定度', max_digits=15, decimal_places=5)
    relative_E = models.CharField(verbose_name='相对不确定度', max_length=20)


    def __str__(self):
        return ("%s %s" % (self.user_name, self.user_num))

    class Meta:
        verbose_name = '杨氏静态模量实验'
        verbose_name_plural = verbose_name
