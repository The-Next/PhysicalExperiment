from django.db import models

# Create your models here.
class ThermalConductivity(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号', blank=True, null=True)
    user_name = models.CharField(verbose_name='学生姓名', max_length=20, blank=True, null=True, default='李华')
    user_num = models.CharField(verbose_name='学生学号', max_length=20, blank=True, null=True, default='1')
    #散热盘降温
    Tp_1 = models.DecimalField(verbose_name='Tp1', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_2 = models.DecimalField(verbose_name='Tp2', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_3 = models.DecimalField(verbose_name='Tp3', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_4 = models.DecimalField(verbose_name='Tp4', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_5 = models.DecimalField(verbose_name='Tp5', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_6 = models.DecimalField(verbose_name='Tp6', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_7 = models.DecimalField(verbose_name='Tp7', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_8 = models.DecimalField(verbose_name='Tp8', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_9 = models.DecimalField(verbose_name='Tp9', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_10 = models.DecimalField(verbose_name='Tp10', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_11 = models.DecimalField(verbose_name='Tp11', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_12 = models.DecimalField(verbose_name='Tp12', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_13 = models.DecimalField(verbose_name='Tp13', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_14 = models.DecimalField(verbose_name='Tp14', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_15 = models.DecimalField(verbose_name='Tp15', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_16 = models.DecimalField(verbose_name='Tp16', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_17 = models.DecimalField(verbose_name='Tp17', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_18 = models.DecimalField(verbose_name='Tp18', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_19 = models.DecimalField(verbose_name='Tp19', max_digits=15, decimal_places=5,null=True,blank=True)
    Tp_20 = models.DecimalField(verbose_name='Tp20', max_digits=15, decimal_places=5,null=True,blank=True)

    #样品厚度
    hb_1 = models.DecimalField(verbose_name='样品厚度1', max_digits=15, decimal_places=5)
    hb_2 = models.DecimalField(verbose_name='样品厚度2', max_digits=15, decimal_places=5)
    hb_3 = models.DecimalField(verbose_name='样品厚度3', max_digits=15, decimal_places=5)
    hb_4 = models.DecimalField(verbose_name='样品厚度4', max_digits=15, decimal_places=5)
    hb_5 = models.DecimalField(verbose_name='样品厚度5', max_digits=15, decimal_places=5)
    hb_6 = models.DecimalField(verbose_name='样品厚度6', max_digits=15, decimal_places=5)

    Ta = models.DecimalField(verbose_name='加热盘稳态', max_digits=15, decimal_places=5)
    Tp = models.DecimalField(verbose_name='散热盘稳态', max_digits=15, decimal_places=5)

    D1 = models.DecimalField(verbose_name='散热盘直径1', max_digits=15, decimal_places=5)
    D2 = models.DecimalField(verbose_name='散热盘直径2', max_digits=15, decimal_places=5)
    D3 = models.DecimalField(verbose_name='散热盘直径3', max_digits=15, decimal_places=5)
    D4 = models.DecimalField(verbose_name='散热盘直径4', max_digits=15, decimal_places=5)
    D5 = models.DecimalField(verbose_name='散热盘直径5', max_digits=15, decimal_places=5)
    D6 = models.DecimalField(verbose_name='散热盘直径6', max_digits=15, decimal_places=5)

    D = models.DecimalField(verbose_name='平均直径', max_digits=15, decimal_places=5)

    m =  models.DecimalField(verbose_name='散热盘质量', max_digits=15, decimal_places=5)
    c =  models.DecimalField(verbose_name='比热容', max_digits=15, decimal_places=5)

    space1 = models.DecimalField(verbose_name='散热时间间隔', max_digits=15, decimal_places=5)
    space2 = models.DecimalField(verbose_name='加热时间间隔', max_digits=15, decimal_places=5)

    p1 = models.CharField(verbose_name='二次方程', max_length=100)
    p2 = models.CharField(verbose_name='导函数', max_length=100)
    t = models.DecimalField(verbose_name='斜率', max_digits=15, decimal_places=5)
    # 这两个字段只是为了绕过序列化器而存在
    img1 = models.CharField(max_length=100,verbose_name='升温曲线')
    img2 = models.CharField(max_length=100,verbose_name='降温曲线')


    img10 = models.ImageField(upload_to='images/ThermalConductivity/%Y/%m/%d',verbose_name='升温曲线',null=True,blank=True)
    img20 = models.ImageField(upload_to='images/ThermalConductivity/%Y/%m/%d',verbose_name='降温曲线',null=True,blank=True)


    k = models.DecimalField(verbose_name='导热系数', max_digits=15, decimal_places=5)

    def __str__(self):
        return ("%s %s" % (self.user_name, self.user_num))

    def save(self, *args, **kwargs):
        self.img10=self.img1
        self.img20=self.img2
        super(ThermalConductivity, self).save(*args, **kwargs)

    class Meta:
        verbose_name = '非良导体热导率实验'
        verbose_name_plural = verbose_name