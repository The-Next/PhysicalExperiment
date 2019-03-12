from django.db import models

# Create your models here.

class Spectrometer(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号', blank=True, null=True)
    user_name = models.CharField(verbose_name='学生姓名', max_length=20, blank=True, null=True, default='李华')
    user_num = models.CharField(verbose_name='学生学号', max_length=20, blank=True, null=True, default='1')
    #测量值
    phi1_1 = models.CharField(verbose_name='&phi;<sub>1</sub>', max_length=30)
    phi2_1 = models.CharField(verbose_name='&phi;<sub>2</sub>', max_length=30)
    phi3_1 = models.CharField(verbose_name='&phi;\'<sub>1</sub>', max_length=30)
    phi4_1 = models.CharField(verbose_name='&phi;\'<sub>2</sub>', max_length=30)
    phi1_2 = models.CharField(verbose_name='&phi;<sub>1</sub>', max_length=30)
    phi2_2 = models.CharField(verbose_name='&phi;<sub>2</sub>', max_length=30)
    phi3_2 = models.CharField(verbose_name='&phi;\'<sub>1</sub>', max_length=30)
    phi4_2 = models.CharField(verbose_name='&phi;\'<sub>2</sub>', max_length=30)
    phi1_3 = models.CharField(verbose_name='&phi;<sub>1</sub>', max_length=30)
    phi2_3 = models.CharField(verbose_name='&phi;<sub>2</sub>', max_length=30)
    phi3_3 = models.CharField(verbose_name='&phi;\'<sub>1</sub>', max_length=30)
    phi4_3 = models.CharField(verbose_name='&phi;\'<sub>2</sub>', max_length=30)
    phi1_4 = models.CharField(verbose_name='&phi;<sub>1</sub>', max_length=30)
    phi2_4 = models.CharField(verbose_name='&phi;<sub>2</sub>', max_length=30)
    phi3_4 = models.CharField(verbose_name='&phi;\'<sub>1</sub>', max_length=30)
    phi4_4 = models.CharField(verbose_name='&phi;\'<sub>2</sub>', max_length=30)
    phi1_5 = models.CharField(verbose_name='&phi;<sub>1</sub>', max_length=30)
    phi2_5 = models.CharField(verbose_name='&phi;<sub>2</sub>', max_length=30)
    phi3_5 = models.CharField(verbose_name='&phi;\'<sub>1</sub>', max_length=30)
    phi4_5 = models.CharField(verbose_name='&phi;\'<sub>2</sub>', max_length=30)
    phi1_6 = models.CharField(verbose_name='&phi;<sub>1</sub>', max_length=30)
    phi2_6 = models.CharField(verbose_name='&phi;<sub>2</sub>', max_length=30)
    phi3_6 = models.CharField(verbose_name='&phi;\'<sub>1</sub>', max_length=30)
    phi4_6 = models.CharField(verbose_name='&phi;\'<sub>2</sub>', max_length=30)
    Instrumenttolerance = models.CharField(verbose_name='分光计仪器允差', max_length=30,default='1\'')
    #自准法测量顶角的补角
    phi1 = models.CharField(
        verbose_name='1/2(|&phi;<sub>1</sub>-&phi;<sub>2</sub>|+|&phi;\'<sub>1</sub>-&phi;\'<sub>2</sub>|)',
        max_length=30)
    phi2 = models.CharField(
        verbose_name='1/2(|&phi;<sub>1</sub>-&phi;<sub>2</sub>|+|&phi;\'<sub>1</sub>-&phi;\'<sub>2</sub>|)',
        max_length=30)
    phi3 = models.CharField(
        verbose_name='1/2(|&phi;<sub>1</sub>-&phi;<sub>2</sub>|+|&phi;\'<sub>1</sub>-&phi;\'<sub>2</sub>|)',
        max_length=30)
    phi4 = models.CharField(
        verbose_name='1/2(|&phi;<sub>1</sub>-&phi;<sub>2</sub>|+|&phi;\'<sub>1</sub>-&phi;\'<sub>2</sub>|)',
        max_length=30)
    phi5 = models.CharField(
        verbose_name='1/2(|&phi;<sub>1</sub>-&phi;<sub>2</sub>|+|&phi;\'<sub>1</sub>-&phi;\'<sub>2</sub>|)',
        max_length=30)
    phi6 = models.CharField(
        verbose_name='1/2(|&phi;<sub>1</sub>-&phi;<sub>2</sub>|+|&phi;\'<sub>1</sub>-&phi;\'<sub>2</sub>|)',
        max_length=30)
    alpha = models.CharField(verbose_name='顶角',max_length=30)
    phiba = models.CharField(verbose_name='角度平均值',max_length=30)
    delta = models.CharField(verbose_name='不确定度',max_length=30)

    def __str__(self):
        return "%s  %s"%(self.user_num,self.user_name)

    class Meta:
        verbose_name = '分光计的调整与使用'
        verbose_name_plural=verbose_name


