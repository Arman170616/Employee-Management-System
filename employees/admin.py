from django.contrib import admin
from .models import Department, Employee, DeptManager, DeptEmp, Title, Salary

admin.site.register(Department)
admin.site.register(Employee)
admin.site.register(DeptManager)
admin.site.register(DeptEmp)
admin.site.register(Title)
admin.site.register(Salary)
