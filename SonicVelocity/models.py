from django.db import models

# Create your models here.
'''
class SonicVelocity(models.Model):
    #频率
    f_1 = models.DecimalField(verbose_name='频率1', max_digits=10, decimal_places=6)
    f_2 = models.DecimalField(verbose_name='频率2', max_digits=10, decimal_places=6)
    f_3 = models.DecimalField(verbose_name='频率3', max_digits=10, decimal_places=6)
    f_4 = models.DecimalField(verbose_name='频率4', max_digits=10, decimal_places=6)
    f_5 = models.DecimalField(verbose_name='频率5', max_digits=10, decimal_places=6)
    f_6 = models.DecimalField(verbose_name='频率6', max_digits=10, decimal_places=6)
    f_avg = models.DecimalField(verbose_name='平均频率', max_digits=10, decimal_places=6)

    #共振干涉法参数
    Rl1 = models.DecimalField(verbose_name='位置1', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl2 = models.DecimalField(verbose_name='位置2', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl3 = models.DecimalField(verbose_name='位置3', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl4 = models.DecimalField(verbose_name='位置4', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl5 = models.DecimalField(verbose_name='位置5', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl6 = models.DecimalField(verbose_name='位置6', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl7 = models.DecimalField(verbose_name='位置7', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl8 = models.DecimalField(verbose_name='位置8', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl9 = models.DecimalField(verbose_name='位置9', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl10 = models.DecimalField(verbose_name='位置10', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl11 = models.DecimalField(verbose_name='位置11', max_digits=10, decimal_places=6,null=True,blank=True)
    Rl12 = models.DecimalField(verbose_name='位置12', max_digits=10, decimal_places=6,null=True,blank=True)

    #相位比较法参数
    Ll1 = models.DecimalField(verbose_name='位置1', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll2 = models.DecimalField(verbose_name='位置2', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll3 = models.DecimalField(verbose_name='位置3', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll4 = models.DecimalField(verbose_name='位置4', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll5 = models.DecimalField(verbose_name='位置5', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll6 = models.DecimalField(verbose_name='位置6', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll7 = models.DecimalField(verbose_name='位置7', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll8 = models.DecimalField(verbose_name='位置8', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll9 = models.DecimalField(verbose_name='位置9', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll10 = models.DecimalField(verbose_name='位置10', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll11 = models.DecimalField(verbose_name='位置11', max_digits=10, decimal_places=6, null=True, blank=True)
    Ll12 = models.DecimalField(verbose_name='位置12', max_digits=10, decimal_places=6, null=True, blank=True)

    #时差法位置参数
    Fl1 = models.DecimalField(verbose_name='位置1', max_digits=10, decimal_places=6, null=True, blank=True)
    Fl2 = models.DecimalField(verbose_name='位置2', max_digits=10, decimal_places=6, null=True, blank=True)
    Fl3 = models.DecimalField(verbose_name='位置3', max_digits=10, decimal_places=6, null=True, blank=True)
    Fl4 = models.DecimalField(verbose_name='位置4', max_digits=10, decimal_places=6, null=True, blank=True)
    Fl5 = models.DecimalField(verbose_name='位置5', max_digits=10, decimal_places=6, null=True, blank=True)
    Fl6 = models.DecimalField(verbose_name='位置6', max_digits=10, decimal_places=6, null=True, blank=True)

    #时差法时间参数
    T_1 = models.DecimalField(verbose_name='时间1', max_digits=10, decimal_places=6, null=True, blank=True)
    T_2 = models.DecimalField(verbose_name='时间2', max_digits=10, decimal_places=6, null=True, blank=True)
    T_3 = models.DecimalField(verbose_name='时间3', max_digits=10, decimal_places=6, null=True, blank=True)
    T_4 = models.DecimalField(verbose_name='时间4', max_digits=10, decimal_places=6, null=True, blank=True)
    T_5 = models.DecimalField(verbose_name='时间5', max_digits=10, decimal_places=6, null=True, blank=True)
    T_6 = models.DecimalField(verbose_name='时间6', max_digits=10, decimal_places=6, null=True, blank=True)

    #不确定度
    uncertainty_v = models.DecimalField(verbose_name='游标卡尺不确定度', max_digits=10, decimal_places=6, null=True, blank=True)
    uncertainty_t = models.DecimalField(verbose_name='计时器不确定度', max_digits=10, decimal_places=6, null=True, blank=True)


    # 温度
    t = models.DecimalField(verbose_name='温度', max_digits=10, decimal_places=6)
    # 该室温下声速
    V = models.DecimalField(verbose_name='该室温下声速', max_digits=10, decimal_places=6)

    #共振干涉法求得声速
    V1 = models.DecimalField(verbose_name='共振干涉法理论声速', max_digits=10, decimal_places=6)
    uncertainty1 = models.DecimalField(verbose_name='共振干涉法声速不确定度', max_digits=10, decimal_places=6)
    #与理论值偏差
    A1 = models.CharField(verbose_name='与理论值偏差',max_length=30)

    # 相位比较法求得声速
    V2 = models.DecimalField(verbose_name='相位比较法理论声速', max_digits=10, decimal_places=6)
    uncertainty2 = models.DecimalField(verbose_name='相位比较法声速不确定度', max_digits=10, decimal_places=6)
    # 与理论值偏差
    A2 = models.CharField(verbose_name='与理论值偏差', max_length=30)

    # 时差求得声速
    V3 = models.DecimalField(verbose_name='时差法法理论声速', max_digits=10, decimal_places=6)
    uncertainty3 = models.DecimalField(verbose_name='时差法法声速不确定度', max_digits=10, decimal_places=6)
    # 与理论值偏差
    A3 = models.CharField(verbose_name='与理论值偏差', max_length=30)


'''
