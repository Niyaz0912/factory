from django import forms
from .models import ShiftAssignment


class ShiftAssignmentForm(forms.ModelForm):
    class Meta:
        model = ShiftAssignment
        fields = ['batch_number', 'operation_name', 'quantity', 'operator', 'part_id', 'machine_id']
