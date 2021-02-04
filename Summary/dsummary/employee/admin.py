from django.contrib import admin

# Register your models here.
from .models import Employee, Department
from simple_history.admin import SimpleHistoryAdmin

# admin.py

from django.contrib import admin
from .models import Employee, Department

# Register your models here.

#class EmployeeAdmin(admin.ModelAdmin):
class EmployeeAdmin(SimpleHistoryAdmin):
    list_display = ['first_name', 'last_name', 'department']
    list_filter = ['department']

class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
