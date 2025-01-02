from django import forms
from users.forms import StyleFormMixin
from shift_assignment.models import ShiftAssignment, CompletedShiftAssignment


class ShiftAssignmentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = ShiftAssignment
        fields = ['batch_number', 'operation_name', 'quantity', 'operator', 'part_id', 'machine_id']


class CompletedShiftAssignmentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = CompletedShiftAssignment
        fields = ['operator', 'operation_name', 'machine_id', 'part_id', 'batch_number', 'quantity', 'defect_quantity',
                  'stop_reason']
