from django.contrib import admin
from Experimentation.models import *
# Register your models here.
@admin.register(NewTown)
class NewTownAdmin(admin.ModelAdmin):
    fieldsets =  (
        (None, {'fields': ('user_id','user_name', 'user_num')}),
        (('实验参数'),{'fields': ('Instrumenttolerance', 'lamda')}),
        (('左侧数据'), {'fields': ('l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l25', 'l26', 'l27', 'l28', 'l29', 'l30')}),
        (('右侧数据'), {'fields': ('r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30')}),
        (('各环直径'), {'fields': ('d5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd25', 'd26', 'd27', 'd28', 'd29', 'd30')}),
        (('每一组所得曲率半径'), {'fields': ('r30_10', 'r29_9', 'r28_8', 'r27_7', 'r26_6', 'r25_5')}),
        (('半径平方差'), {'fields': ('value30_10', 'value29_9', 'value28_8', 'value27_7', 'value26_6', 'value25_5')}),
        (('最终结果'), {'fields': ('uncertainty', 'anwser')}),
    )
    list_display = ('id','user_name','user_num')