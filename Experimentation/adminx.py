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
                       'l5', 'l6', 'l7', 'l8', 'l9', 'l10', 'l25', 'l26', 'l27', 'l28', 'l29', 'l30',
                       'r5', 'r6', 'r7', 'r8', 'r9', 'r10', 'r25', 'r26', 'r27', 'r28', 'r29', 'r30',
                       'd5', 'd6', 'd7', 'd8', 'd9', 'd10', 'd25', 'd26', 'd27', 'd28', 'd29', 'd30',
                       'value30_10', 'value29_9', 'value28_8', 'value27_7', 'value26_6', 'value25_5',
                       'r30_10', 'r29_9', 'r28_8', 'r27_7', 'r26_6', 'r25_5',
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
                             Row('l5', 'r5', 'd5'),
                             Row('l6', 'r6', 'd6'),
                             Row('l7', 'r7', 'd7'),
                             Row('l8', 'r8', 'd8'),
                             Row('l9', 'r9', 'd9'),
                             Row('l10', 'r10', 'd10'),
                             Row('l25', 'r25', 'd25'),
                             Row('l26', 'r26', 'd26'),
                             Row('l27', 'r27', 'd27'),
                             Row('l28', 'r28', 'd28'),
                             Row('l29', 'r29', 'd29'),
                             Row('l30', 'r30', 'd30'),
                            ),

                    Fieldset(('各组数据对应半径平方差与曲率半径'),
                             Col('','value30_10', 'value29_9', 'value28_8', 'value27_7', 'value26_6', 'value25_5'),
                             Col('','r30_10', 'r29_9', 'r28_8', 'r27_7', 'r26_6', 'r25_5'),
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