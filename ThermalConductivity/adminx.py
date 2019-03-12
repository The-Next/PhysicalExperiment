from extra_apps import xadmin
from ThermalConductivity.models import *
# Register your models here.
from extra_apps.xadmin.layout import Main, Fieldset, Row, Col, HTML, Side


class ThermalConductivityAdmin():
    list_display = ('user_name','user_num')
    search_fields = ('user_name', 'user_num')
    list_filter = ('user_num','user_name')

    save_as = False

    def get_form_layout(self):
        if self.org_obj:
            self.form_layout = (
                Main(
                    Fieldset('',
                             'user_name', 'user_num', 'user_id',
                             css_class='unsort no_title'
                             ),
                    Fieldset(('实验参数'),
                             ),
                    Fieldset(('测量值'),
                             ),

                    Fieldset((''),
                             ),

                ),
                Side(
                    Fieldset(('最终结果'),
                             ),
                )

            )
        return super(ThermalConductivityAdmin, self).get_form_layout()

    class Meta():
        verbose_name = '热导率实验'


xadmin.site.register(ThermalConductivity, ThermalConductivityAdmin)