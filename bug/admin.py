from django.contrib import admin

# Register your models here.
from bug.models import Bug



class BugAdmin(admin.ModelAdmin):
    list_display = ['bugname ', 'bugdetail ', ' bugstatus', ' buglevel', ' bugcreater', ' bugassign', 'create_time','id']

#把bug模块注册到Djangoadmin后太管理并且能显示
admin.site.register(Bug)