from django.db import models
from LoginValidation.models import User
# Create your models here.
class NewTown(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号',blank=True,null=True)
    user_name = models.CharField(verbose_name='学生姓名',max_length=20,blank=True,null=True,default='李华')
    user_num = models.CharField(verbose_name='学生学号',max_length=20,blank=True,null=True,default='1')
    l5 = models.DecimalField(verbose_name='左边第5个读数(mm)',max_digits=10, decimal_places=4)
    l6 = models.DecimalField(verbose_name='左边第6个读数(mm)',max_digits=10, decimal_places=4)
    l7 = models.DecimalField(verbose_name='左边第7个读数(mm)',max_digits=10, decimal_places=4)
    l8 = models.DecimalField(verbose_name='左边第8个读数(mm)',max_digits=10, decimal_places=4)
    l9 = models.DecimalField(verbose_name='左边第9个读数(mm)',max_digits=10, decimal_places=4)
    l10 = models.DecimalField(verbose_name='左边第10个读数(mm)', max_digits=10, decimal_places=4)
    l25 = models.DecimalField(verbose_name='左边第25个读数(mm)',max_digits=10, decimal_places=4)
    l26 = models.DecimalField(verbose_name='左边第26个读数(mm)',max_digits=10, decimal_places=4)
    l27 = models.DecimalField(verbose_name='左边第27个读数(mm)',max_digits=10, decimal_places=4)
    l28 = models.DecimalField(verbose_name='左边第28个读数(mm)',max_digits=10, decimal_places=4)
    l29 = models.DecimalField(verbose_name='左边第29个读数(mm)',max_digits=10, decimal_places=4)
    l30 = models.DecimalField(verbose_name='左边第30个读数(mm)',max_digits=10, decimal_places=4)

    r5 = models.DecimalField(verbose_name='右边第5个读数(mm)',max_digits=10, decimal_places=4)
    r6 = models.DecimalField(verbose_name='右边第6个读数(mm)',max_digits=10, decimal_places=4)
    r7 = models.DecimalField(verbose_name='右边第7个读数(mm)',max_digits=10, decimal_places=4)
    r8 = models.DecimalField(verbose_name='右边第8个读数(mm)',max_digits=10, decimal_places=4)
    r9 = models.DecimalField(verbose_name='右边第9个读数(mm)',max_digits=10, decimal_places=4)
    r10 = models.DecimalField(verbose_name='右边第10个读数(mm)',max_digits=10, decimal_places=4)
    r25 = models.DecimalField(verbose_name='右边第25个读数(mm)',max_digits=10, decimal_places=4)
    r26 = models.DecimalField(verbose_name='右边第26个读数(mm)',max_digits=10, decimal_places=4)
    r27 = models.DecimalField(verbose_name='右边第27个读数(mm)',max_digits=10, decimal_places=4)
    r28 = models.DecimalField(verbose_name='右边第28个读数(mm)',max_digits=10, decimal_places=4)
    r29 = models.DecimalField(verbose_name='右边第29个读数(mm)',max_digits=10, decimal_places=4)
    r30 = models.DecimalField(verbose_name='右边第30个读数(mm)',max_digits=10, decimal_places=4)

    d5 = models.DecimalField(verbose_name='第5个环直径(mm)',max_digits=10, decimal_places=4)
    d6 = models.DecimalField(verbose_name='第6个环直径(mm)',max_digits=10, decimal_places=4)
    d7 = models.DecimalField(verbose_name='第7个环直径(mm)',max_digits=10, decimal_places=4)
    d8 = models.DecimalField(verbose_name='第8个环直径(mm)',max_digits=10, decimal_places=4)
    d9 = models.DecimalField(verbose_name='第9个环直径(mm)',max_digits=10, decimal_places=4)
    d10 = models.DecimalField(verbose_name='第10个环直径(mm)', max_digits=10, decimal_places=4)
    d25 = models.DecimalField(verbose_name='第25个环直径(mm)',max_digits=10, decimal_places=4)
    d26 = models.DecimalField(verbose_name='第26个环直径(mm)',max_digits=10, decimal_places=4)
    d27 = models.DecimalField(verbose_name='第27个环直径(mm)',max_digits=10, decimal_places=4)
    d28 = models.DecimalField(verbose_name='第28个环直径(mm)',max_digits=10, decimal_places=4)
    d29 = models.DecimalField(verbose_name='第29个环直径(mm)',max_digits=10, decimal_places=4)
    d30 = models.DecimalField(verbose_name='第30个环直径(mm)',max_digits=10, decimal_places=4)

    r30_10 = models.DecimalField(verbose_name='30与10所得的曲率半径',max_digits=10, decimal_places=4)
    r29_9 = models.DecimalField(verbose_name='29与9所得的曲率半径',max_digits=10, decimal_places=4)
    r28_8 = models.DecimalField(verbose_name='28与8所得的曲率半径',max_digits=10, decimal_places=4)
    r27_7 = models.DecimalField(verbose_name='27与7所得的曲率半径',max_digits=10, decimal_places=4)
    r26_6 = models.DecimalField(verbose_name='26与6所得的曲率半径',max_digits=10, decimal_places=4)
    r25_5 = models.DecimalField(verbose_name='25与5所得的曲率半径',max_digits=10, decimal_places=4)

    value30_10 = models.DecimalField(verbose_name='30与10半径平方差',max_digits=10, decimal_places=4)
    value29_9 = models.DecimalField(verbose_name='29与9半径平方差',max_digits=10, decimal_places=4)
    value28_8 = models.DecimalField(verbose_name='28与8半径平方差',max_digits=10, decimal_places=4)
    value27_7 = models.DecimalField(verbose_name='27与7半径平方差',max_digits=10, decimal_places=4)
    value26_6 = models.DecimalField(verbose_name='26与6半径平方差',max_digits=10, decimal_places=4)
    value25_5 = models.DecimalField(verbose_name='25与5半径平方差',max_digits=10, decimal_places=4)

    Instrumenttolerance = models.DecimalField(verbose_name='仪器允差(mm)',max_digits=10, decimal_places=4)
    lamda = models.DecimalField(verbose_name='波长(nm)',max_digits=10, decimal_places=4)
    uncertainty = models.DecimalField(verbose_name='不确定度(m)',max_digits=10, decimal_places=4)
    anwser = models.DecimalField(verbose_name='曲率半径(m)',max_digits=10, decimal_places=4)

    def __str__(self):
        return "%s %s"%(self.user_name,self.user_num)
    class Meta:
        verbose_name = '牛顿环实验'
        verbose_name_plural = verbose_name