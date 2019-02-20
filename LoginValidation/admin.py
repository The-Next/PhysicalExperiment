from django.contrib import admin

# Register your models here.
from django.contrib.auth.admin import UserAdmin
#from django.contrib.auth.models import User

from LoginValidation.models import User

'''class ProfileInline(admin.StackedInline):
    model = UserProfile
    max_num = 1
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = [ProfileInline,]

admin.site.unregister(User)
admin.site.register(User,CustomUserAdmin)'''
@admin.register(User)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {'fields': ('username', 'password','s_num')}),
        (('用户信息'), {'fields': ('first_name', 'email')}),
        (('用户权限'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (('日期信息'), {'fields': ('last_login', 'date_joined')}),
    )
    list_display = ('username', 's_num')

