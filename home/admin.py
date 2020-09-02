from django.contrib import admin
from .models import Qabul, Setting

# Register your models here.
class SettingAdmin(admin.ModelAdmin):
    list_display = ['title', 'title2', 'company']


class QabulAdmin(admin.ModelAdmin):
    list_display = ['name', 'update_at', 'phone', 'direction_of_study', 'status', 'photo3x4', ]
    list_filter = ['status', 'direction_of_study']
    #readonly_fields = ('name', 'ip')



admin.site.register(Setting,SettingAdmin)
admin.site.register(Qabul, QabulAdmin)