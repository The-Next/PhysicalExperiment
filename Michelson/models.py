from django.db import models

# Create your models here.
class Michelson(models.Model):
    user_id = models.IntegerField(verbose_name='学生编号', blank=True, null=True)
    user_name = models.CharField(verbose_name='学生姓名', max_length=20, blank=True, null=True, default='李华')
    user_num = models.CharField(verbose_name='学生学号', max_length=20, blank=True, null=True, default='1')
    '''输入参数列表'''
    one = models.DecimalField(verbose_name='d<sub>1</sub>(mm)',max_digits=10, decimal_places=6)
    two = models.DecimalField(verbose_name='d<sub>2</sub>(mm)',max_digits=10,decimal_places=6)
    three = models.DecimalField(verbose_name='d<sub>3</sub>(mm)',max_digits=10,decimal_places=6)
    four = models.DecimalField(verbose_name='d<sub>4</sub>(mm)',max_digits=10,decimal_places=6)
    five = models.DecimalField(verbose_name='d<sub>5</sub>(mm)',max_digits=10,decimal_places=6)
    six = models.DecimalField(verbose_name='d<sub>6</sub>(mm)',max_digits=10,decimal_places=6)
    seven = models.DecimalField(verbose_name='d<sub>7</sub>(mm)',max_digits=10,decimal_places=6)
    eight = models.DecimalField(verbose_name='d<sub>8</sub>(mm)',max_digits=10,decimal_places=6)
    nine = models.DecimalField(verbose_name='d<sub>9</sub>(mm)',max_digits=10,decimal_places=6)
    ten = models.DecimalField(verbose_name='d<sub>10</sub>(mm)',max_digits=10,decimal_places=6)
    eleven = models.DecimalField(verbose_name='d<sub>11</sub>(mm)',max_digits=10,decimal_places=6)
    twelfth = models.DecimalField(verbose_name='d<sub>12</sub>(mm)',max_digits=10,decimal_places=6)

    '''差值的绝对值'''
    seven_one = models.DecimalField(verbose_name='△d=d<sub>7</sub>-d<sub>1</sub>(mm)',max_digits=10,decimal_places=6)
    eight_two = models.DecimalField(verbose_name='△d=d<sub>8</sub>-d<sub>2</sub>(mm)',max_digits=10,decimal_places=6)
    nine_three = models.DecimalField(verbose_name='△d=d<sub>9</sub>-d<sub>3</sub>(mm)',max_digits=10,decimal_places=6)
    ten_four = models.DecimalField(verbose_name='△d=d<sub>10</sub>-d<sub>4</sub>(mm)',max_digits=10,decimal_places=6)
    eleven_five = models.DecimalField(verbose_name='△d=d<sub>11</sub>-d<sub>5</sub>(mm)',max_digits=10,decimal_places=6)
    twelfth_six = models.DecimalField(verbose_name='△d=d<sub>12</sub>-d<sub>6</sub>(mm)',max_digits=10,decimal_places=6)

    '''结果参数'''
    deltad = models.DecimalField(verbose_name= 'd的平均值(mm)',max_digits=10,decimal_places=6)
    deltadD = models.DecimalField(verbose_name='△d的不确定度(mm)',max_digits=10,decimal_places=6)
    lambda_avg = models.DecimalField(verbose_name='&#923;平均值(nm)',max_digits=10,decimal_places=6)
    deltadlambda = models.DecimalField(verbose_name='&#923;不确定度(nm)',max_digits=10,decimal_places=6)
    E = models.CharField(verbose_name='相对不确定度',max_length=20)
    '''参数'''
    Instrumenttolerance = models.DecimalField(verbose_name='仪器允差(mm)',max_digits=10,decimal_places=6)

    def __str__(self):
        return ("%s %s"%(self.user_name,self.user_num))

    class Meta:
        verbose_name = '迈克尔逊干涉仪实验'
        verbose_name_plural = verbose_name