import xadmin
from xadmin import views
from xadmin.plugins.auth import UserAdmin

from LoginValidation.models import User

'''xadmin.site.unregister(User)
       @xadmin.site.register(User)
       class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','s_num')}),
        (('用户信息'), {'fields': ('first_name', 'email')}),
        (('用户权限'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('日期信息'), {'fields': ('last_login', 'date_joined')}),
    )list_display = ('username', 's_num')
    '''

# 后台系统名称页脚设置、设置后台菜单为收缩样式
class GlobalSetting(object):
    site_title = '物理实验后台管理系统'
    site_footer = 'zzuli.com'
    menu_style = 'accordion'


xadmin.site.register(views.CommAdminView, GlobalSetting)