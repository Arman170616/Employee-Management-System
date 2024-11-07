# employees/forms.py

from django import forms
from .models import Employee, Department

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_no', 'birth_date', 'first_name', 'last_name', 'gender', 'hire_date']
        widgets = {
            'birth_date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
            'hire_date': forms.DateInput(attrs={'type': 'date', 'class': 'input'}),
        }

class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['dept_no', 'dept_name']
        widgets = {
            'dept_no': forms.TextInput(attrs={'class': 'input'}),
            'dept_name': forms.TextInput(attrs={'class': 'input'}),
        }
