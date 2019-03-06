from extra_apps import xadmin
from extra_apps.xadmin.layout import Main, Fieldset, Row, Col, Side

from StaticYoungModulus.models import *
# Register your models here.

class StataicYounyModulusAdmin():
    list_display = ('user_name','user_num')
    search_fields = ('user_name', 'user_num')
    list_filter = ('user_num','user_name')

    readonly_fields = [
        'user_name', 'user_num', 'user_id',
        'L', 'D', 'K',
        'delta_L', 'delta_D', 'delta_K',
        'n0', 'n_0', 'n0_avg',
        'n1', 'n_1', 'n1_avg',
        'n2', 'n_2', 'n2_avg',
        'n3', 'n_3', 'n3_avg',
        'n4', 'n_4', 'n4_avg',
        'n5', 'n_5', 'n5_avg',
        'n6', 'n_6', 'n6_avg',
        'n7', 'n_7', 'n7_avg',
        'd1','d2','d3','d4','d5','d6','d_avg',
        'n4_0','n5_1','n6_2','n7_3','ln',
        'delta_dn', 'delta_ln', 'E', 'delta_E', 'relative_E',
        'micrometer', 'verniercaliper',

    ]

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'user_name', 'user_num','user_id',
                             css_class='unsort no_title'
                             ),
                    Fieldset(('实验参数'),
                             Row('L','D','K'),
                             Row('delta_L','delta_D','delta_K'),
                             Row('micrometer','verniercaliper'),
                    ),
                    Fieldset(('测量值'),
                             Row('n0', 'n_0', 'n0_avg'),
                             Row('n1', 'n_1', 'n1_avg'),
                             Row('n2', 'n_2', 'n2_avg'),
                             Row('n3', 'n_3', 'n3_avg'),
                             Row('n4', 'n_4', 'n4_avg'),
                             Row('n5', 'n_5', 'n5_avg'),
                             Row('n6', 'n_6', 'n6_avg'),
                             Row('n7', 'n_7', 'n7_avg'),
                             ),
                    Fieldset(('直径'),
                             Row('d1'),
                             Row('d2'),
                             Row('d3'),
                             Row('d4'),
                             Row('d5'),
                             Row('d6'),
                             Row('d_avg'),
                    ),
                    Fieldset(('逐差法计算过程'),
                             Row('n4_0'),
                             Row('n5_1'),
                             Row('n6_2'),
                             Row('n7_3'),
                             'ln',
                             )
                ),
                Side(
                    Fieldset(('最终结果'),
                             'delta_dn', 'delta_ln','E','delta_E','relative_E',
                             ),
                )
            )
        return super(StataicYounyModulusAdmin, self).get_form_layout()

    class Meta():
        verbose_name = '杨氏静态模量实验'

xadmin.site.register(StaticYooungModulus,StataicYounyModulusAdmin)