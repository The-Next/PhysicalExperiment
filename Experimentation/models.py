from django.db import models
from LoginValidation.models import User
# Create your models here.
class NewTown(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号',blank=True,null=True)
    user_name = models.CharField(verbose_name='学生姓名',max_length=20,blank=True,null=True,default='李华')
    user_num = models.CharField(verbose_name='学生学号',max_length=20,blank=True,null=True,default='1')
    l10 = models.DecimalField(verbose_name='左边第10个读数(mm)',max_digits=10, decimal_places=4)#
    l11 = models.DecimalField(verbose_name='左边第11个读数(mm)',max_digits=10, decimal_places=4)#
    l12 = models.DecimalField(verbose_name='左边第12个读数(mm)',max_digits=10, decimal_places=4)#
    l13 = models.DecimalField(verbose_name='左边第13个读数(mm)',max_digits=10, decimal_places=4)#
    l14 = models.DecimalField(verbose_name='左边第14个读数(mm)',max_digits=10, decimal_places=4)#
    l15 = models.DecimalField(verbose_name='左边第15个读数(mm)', max_digits=10, decimal_places=4)#
    l30 = models.DecimalField(verbose_name='左边第30个读数(mm)',max_digits=10, decimal_places=4)#
    l31 = models.DecimalField(verbose_name='左边第31个读数(mm)',max_digits=10, decimal_places=4)#
    l32 = models.DecimalField(verbose_name='左边第32个读数(mm)',max_digits=10, decimal_places=4)#
    l33 = models.DecimalField(verbose_name='左边第33个读数(mm)',max_digits=10, decimal_places=4)#
    l34 = models.DecimalField(verbose_name='左边第34个读数(mm)',max_digits=10, decimal_places=4)#
    l35= models.DecimalField(verbose_name='左边第35个读数(mm)',max_digits=10, decimal_places=4)#
    #
    r10 = models.DecimalField(verbose_name='右边第10个读数(mm)',max_digits=10, decimal_places=4)#
    r11 = models.DecimalField(verbose_name='右边第11个读数(mm)',max_digits=10, decimal_places=4)#
    r12 = models.DecimalField(verbose_name='右边第12个读数(mm)',max_digits=10, decimal_places=4)#
    r13 = models.DecimalField(verbose_name='右边第13个读数(mm)',max_digits=10, decimal_places=4)#
    r14 = models.DecimalField(verbose_name='右边第14个读数(mm)',max_digits=10, decimal_places=4)#
    r15 = models.DecimalField(verbose_name='右边第15个读数(mm)',max_digits=10, decimal_places=4)#
    r30 = models.DecimalField(verbose_name='右边第30个读数(mm)',max_digits=10, decimal_places=4)#
    r31 = models.DecimalField(verbose_name='右边第31个读数(mm)',max_digits=10, decimal_places=4)#
    r32 = models.DecimalField(verbose_name='右边第32个读数(mm)',max_digits=10, decimal_places=4)#
    r33 = models.DecimalField(verbose_name='右边第33个读数(mm)',max_digits=10, decimal_places=4)#
    r34 = models.DecimalField(verbose_name='右边第34个读数(mm)',max_digits=10, decimal_places=4)#
    r35 = models.DecimalField(verbose_name='右边第35个读数(mm)',max_digits=10, decimal_places=4)#

    d10 = models.DecimalField(verbose_name='第10个环直径(mm)',max_digits=10, decimal_places=4)#
    d11 = models.DecimalField(verbose_name='第11个环直径(mm)',max_digits=10, decimal_places=4)#
    d12 = models.DecimalField(verbose_name='第12个环直径(mm)',max_digits=10, decimal_places=4)#
    d13 = models.DecimalField(verbose_name='第13个环直径(mm)',max_digits=10, decimal_places=4)#
    d14 = models.DecimalField(verbose_name='第14个环直径(mm)',max_digits=10, decimal_places=4)#
    d15 = models.DecimalField(verbose_name='第15个环直径(mm)', max_digits=10, decimal_places=4)#
    d30 = models.DecimalField(verbose_name='第30个环直径(mm)',max_digits=10, decimal_places=4)#
    d31 = models.DecimalField(verbose_name='第31个环直径(mm)',max_digits=10, decimal_places=4)#
    d32 = models.DecimalField(verbose_name='第32个环直径(mm)',max_digits=10, decimal_places=4)#
    d33 = models.DecimalField(verbose_name='第33个环直径(mm)',max_digits=10, decimal_places=4)#
    d34 = models.DecimalField(verbose_name='第34个环直径(mm)',max_digits=10, decimal_places=4)#
    d35 = models.DecimalField(verbose_name='第35个环直径(mm)',max_digits=10, decimal_places=4)#

    r35_15 = models.DecimalField(verbose_name='35与15所得的曲率半径',max_digits=10, decimal_places=4)
    r34_14 = models.DecimalField(verbose_name='34与14所得的曲率半径',max_digits=10, decimal_places=4)
    r33_13 = models.DecimalField(verbose_name='33与13所得的曲率半径',max_digits=10, decimal_places=4)
    r32_12 = models.DecimalField(verbose_name='32与12所得的曲率半径',max_digits=10, decimal_places=4)
    r31_11 = models.DecimalField(verbose_name='31与11所得的曲率半径',max_digits=10, decimal_places=4)
    r30_10 = models.DecimalField(verbose_name='30与10所得的曲率半径',max_digits=10, decimal_places=4)

    value35_15 = models.DecimalField(verbose_name='35与15半径平方差',max_digits=10, decimal_places=4)
    value34_14 = models.DecimalField(verbose_name='34与14半径平方差',max_digits=10, decimal_places=4)
    value33_13 = models.DecimalField(verbose_name='33与13半径平方差',max_digits=10, decimal_places=4)
    value32_12 = models.DecimalField(verbose_name='32与12半径平方差',max_digits=10, decimal_places=4)
    value31_11 = models.DecimalField(verbose_name='31与11半径平方差',max_digits=10, decimal_places=4)
    value30_10 = models.DecimalField(verbose_name='30与10半径平方差',max_digits=10, decimal_places=4)

    Instrumenttolerance = models.DecimalField(verbose_name='仪器允差(mm)',max_digits=10, decimal_places=4)
    lamda = models.DecimalField(verbose_name='波长(nm)',max_digits=10, decimal_places=4)
    uncertainty = models.DecimalField(verbose_name='不确定度(m)',max_digits=10, decimal_places=4)
    anwser = models.DecimalField(verbose_name='曲率半径(m)',max_digits=10, decimal_places=4)

    def __str__(self):
        return "%s %s"%(self.user_name,self.user_num)
    class Meta:
        verbose_name = '牛顿环实验'
        verbose_name_plural = verbose_name