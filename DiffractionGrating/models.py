from django.db import models

# Create your models here.
class DiffractionGrating(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号', blank=True, null=True)
    user_name = models.CharField(verbose_name='学生姓名', max_length=20, blank=True, null=True, default='李华')
    user_num = models.CharField(verbose_name='学生学号', max_length=20, blank=True, null=True, default='1')

    Beyond_yellow1 = models.CharField(verbose_name='黄外光&phi;<sub>1</sub>',max_length=30)
    Beyond_yellow2 = models.CharField(verbose_name='黄外光&phi;<sub>2</sub>',max_length=30)
    Beyond_yellow3 = models.CharField(verbose_name='黄外光&phi;\'<sub>1</sub>',max_length=30)
    Beyond_yellow4 = models.CharField(verbose_name='黄外光&phi;\'<sub>2</sub>',max_length=30)

    Inside_yellow1 = models.CharField(verbose_name='黄内光&phi;<sub>1</sub>', max_length=30)
    Inside_yellow2 = models.CharField(verbose_name='黄内光&phi;<sub>2</sub>', max_length=30)
    Inside_yellow3 = models.CharField(verbose_name='黄内光&phi;\'<sub>1</sub>', max_length=30)
    Inside_yellow4 = models.CharField(verbose_name='黄内光&phi;\'<sub>2</sub>', max_length=30)

    green1 = models.CharField(verbose_name='绿光&phi;<sub>1</sub>', max_length=30)
    green2 = models.CharField(verbose_name='绿光&phi;<sub>2</sub>', max_length=30)
    green3 = models.CharField(verbose_name='绿光&phi;\'<sub>1</sub>', max_length=30)
    green4 = models.CharField(verbose_name='绿光&phi;\'<sub>2</sub>', max_length=30)

    blue1 = models.CharField(verbose_name='蓝光&phi;<sub>1</sub>', max_length=30)
    blue2 = models.CharField(verbose_name='蓝光&phi;<sub>2</sub>', max_length=30)
    blue3 = models.CharField(verbose_name='蓝光&phi;\'<sub>1</sub>', max_length=30)
    blue4 = models.CharField(verbose_name='蓝光&phi;\'<sub>2</sub>', max_length=30)

    N = models.IntegerField(verbose_name='光栅有效面积内狭缝总数')

    Beyond_yellow_k = models.IntegerField(verbose_name='黄内光光谱级次')
    Inside_yellow_k = models.IntegerField(verbose_name='黄外光光谱级次')
    green_k = models.IntegerField(verbose_name='绿光光谱级次')
    blue_k = models.IntegerField(verbose_name='蓝光光谱级次')

    d = models.DecimalField(verbose_name='光栅常数',max_digits=15, decimal_places=7)

    Beyond_yellow = models.CharField(verbose_name='黄外光衍射角', max_length=30)
    Inside_yellow = models.CharField(verbose_name='黄内光衍射角', max_length=30)
    green = models.CharField(verbose_name='绿光衍射角', max_length=30)
    blue = models.CharField(verbose_name='蓝光衍射角', max_length=30)

    Beyond_yellow_lambda = models.DecimalField(verbose_name='黄外光波长',max_digits=15, decimal_places=7)
    Inside_yellow_lambda = models.DecimalField(verbose_name='黄内光波长',max_digits=15, decimal_places=7)
    green_lambda = models.DecimalField(verbose_name='绿光波长',max_digits=15, decimal_places=7)
    blue_lambda = models.DecimalField(verbose_name='蓝光波长',max_digits=15, decimal_places=7)

    Beyond_yellow_D = models.DecimalField(verbose_name='黄外光色散率',max_digits=15, decimal_places=7)
    Inside_yellow_D = models.DecimalField(verbose_name='黄内光色散率',max_digits=15, decimal_places=7)
    green_D = models.DecimalField(verbose_name='绿光色散率',max_digits=15, decimal_places=7)
    blue_D = models.DecimalField(verbose_name='蓝光色散率',max_digits=15, decimal_places=7)

    Beyond_yellow_R = models.DecimalField(verbose_name='黄外光分辨本领',max_digits=15, decimal_places=7)
    Inside_yellow_R = models.DecimalField(verbose_name='黄内光分辨本领',max_digits=15, decimal_places=7)
    green_R = models.DecimalField(verbose_name='绿光分辨本领',max_digits=15, decimal_places=7)
    blue_R = models.DecimalField(verbose_name='蓝光分辨本领',max_digits=15, decimal_places=7)

    Beyond_yellow_delta_lambda = models.DecimalField(verbose_name='黄外光波长差',max_digits=15, decimal_places=7)
    Inside_yellow_delta_lambda = models.DecimalField(verbose_name='黄外光波长差',max_digits=15, decimal_places=7)
    green_delta_lambda = models.DecimalField(verbose_name='黄外光波长差',max_digits=15, decimal_places=7)
    blue_delta_lambda = models.DecimalField(verbose_name='黄外光波长差',max_digits=15, decimal_places=7)

    def __str__(self):
        return "%s  %s"%(self.user_num,self.user_name)

    class Meta:
        verbose_name = '衍射光栅'
        verbose_name_plural=verbose_name