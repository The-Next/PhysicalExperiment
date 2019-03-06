from extra_apps import xadmin

# Register your models here.
from extra_apps.xadmin.layout import Main, Fieldset, Row, Side
from Michelson.models import Michelson

class MichelsonAdmin():
    list_display = ('user_name','user_num')
    search_fields = {'user_name','user_num'}
    list_filter = {'user_num','user_name'}

    readonly_fields = ['user_name','user_num','user_id',
                       'Instrumenttolerance',
                       'one', 'seven', 'seven_one',
                       'two', 'eight', 'eight_two',
                       'three', 'nine', 'nine_three',
                       'four', 'ten', 'ten_four',
                       'five', 'eleven', 'eleven_five',
                       'six', 'twelfth', 'twelfth_six',
                       'deltad',
                       'deltadD',
                       'lambda_avg',
                       'deltadlambda',
                       'E',
                       ]

    def get_form_layout(selfs):
        if selfs.org_obj:
            selfs.form_layout = (
                Main(
                    Fieldset('',
                             'user_name','user_num','user_id',
                             css_class='unsort no_title'
                             ),
                    Fieldset(('实验参数'),
                             'Instrumenttolerance',
                             ),
                    Fieldset(('测量值及其差值绝对值'),
                             Row('one','seven','seven_one'),
                             Row('two','eight','eight_two'),
                             Row('three','nine','nine_three'),
                             Row('four','ten','ten_four'),
                             Row('five','eleven','eleven_five'),
                             Row('six','twelfth','twelfth_six')
                             ),
                ),
                Side(
                  Fieldset('计算结果',
                           'deltad',
                           'deltadD',
                           'lambda_avg',
                           'deltadlambda',
                           'E',)
                )
            )
        return super(MichelsonAdmin, selfs).get_form_layout()
    class Meta:
            verbose_name = '迈克尔逊干涉仪实验'

xadmin.site.register(Michelson,MichelsonAdmin)