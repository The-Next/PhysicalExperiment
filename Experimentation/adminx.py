import xadmin
from xadmin.layout import Main, Fieldset, Side, Row, Col, HTML

from Experimentation.models import NewTown


class NewTownAdmin():
    '''fieldsets =  (
        (None, {'fields': ('user_id','user_name', 'user_num')}),
        (('实验参数'),{'fields': ('Instrumenttolerance', 'lamda')}),
        (('左侧数据'), {'fields': ('l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l25', 'l26', 'l27', 'l28', 'l29', 'l30')}),
        (('右侧数据'), {'fields': ('r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30')}),
        (('各环直径'), {'fields': ('d5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd25', 'd26', 'd27', 'd28', 'd29', 'd30')}),
        (('每一组所得曲率半径'), {'fields': ('r30_10', 'r29_9', 'r28_8', 'r27_7', 'r26_6', 'r25_5')}),
        (('半径平方差'), {'fields': ('value30_10', 'value29_9', 'value28_8', 'value27_7', 'value26_6', 'value25_5')}),
        (('最终结果'), {'fields': ('uncertainty', 'anwser')}),
    )'''

    list_display = ('user_name','user_num')
    search_fields = ('user_name', 'user_num')
    list_filter = ('user_num','user_name')

    readonly_fields = ['user_name', 'user_num','user_id',
                       'Instrumenttolerance', 'lamda',
                       'l10', 'l11', 'l12', 'l13', 'l14', 'l15', 'l30', 'l31', 'l32', 'l33', 'l34', 'l35',
                       'r10', 'r11', 'r12', 'r13', 'r14', 'r15', 'r30', 'r31', 'r32', 'r33', 'r34', 'r35',
                       'd10', 'd11', 'd12', 'd13', 'd14', 'd15', 'd30', 'd31', 'd32', 'd33', 'd34', 'd35',
                       'value35_15', 'value34_14', 'value33_13', 'value32_12', 'value31_11', 'value30_10',
                       'r35_15', 'r34_14', 'r33_13', 'r32_12', 'r31_11', 'r30_10',
                       'uncertainty', 'anwser']

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'user_name', 'user_num','user_id',
                             css_class='unsort no_title'
                             ),
                    Fieldset(('实验参数'),
                             'Instrumenttolerance', 'lamda'
                             ),
                    Fieldset(('测量值'),
                             Row('l10', 'r10', 'd10'),
                             Row('l11', 'r11', 'd11'),
                             Row('l12', 'r12', 'd12'),
                             Row('l13', 'r13', 'd13'),
                             Row('l14', 'r14', 'd14'),
                             Row('l15', 'r15', 'd15'),
                             Row('l30', 'r30', 'd30'),
                             Row('l31', 'r31', 'd31'),
                             Row('l32', 'r32', 'd32'),
                             Row('l33', 'r33', 'd33'),
                             Row('l34', 'r34', 'd34'),
                             Row('l35', 'r35', 'd35'),
                            ),

                    Fieldset(('各组数据对应半径平方差与曲率半径'),
                             Col('','value35_15', 'value34_14', 'value33_13', 'value32_12', 'value31_11', 'value30_10'),
                             Col('','r35_15', 'r34_14', 'r33_13', 'r32_12', 'r31_11', 'r30_10'),
                             HTML("右侧值{{Experimentation_newtown.l11}}"),
                             ),

                ),
                Side(
                    Fieldset(('最终结果'),
                             'uncertainty', 'anwser',
                             ),
                )

            )
        return super(NewTownAdmin, self).get_form_layout()

    class Meta():
        verbose_name = '牛顿环实验'


xadmin.site.register(NewTown,NewTownAdmin)