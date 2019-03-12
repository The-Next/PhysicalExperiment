from extra_apps import xadmin
from DiffractionGrating.models import *
# Register your models here.
from extra_apps.xadmin.layout import Main, Fieldset, Row, Col, HTML, Side


class DiffractionGratingAdmin():
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
        return super(DiffractionGratingAdmin, self).get_form_layout()

    class Meta():
        verbose_name = '分光计的调整与使用'


xadmin.site.register(DiffractionGrating, DiffractionGratingAdmin)