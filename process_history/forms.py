from django import forms
from process_history.models import ProcessHistory, ShiftAssignment


class ProcessHistoryForm(forms.ModelForm):
    class Meta:
        model = ProcessHistory
        fields = "__all__"


class ProcessHistoryFormShort(forms.ModelForm):
    class Meta:
        model = ProcessHistory
        exclude = ("param3", "param4", "param5")


class ShiftAssignmentForm(forms.ModelForm):
    class Meta:
        model = ShiftAssignment
        fields = [
            'master',
            'operator',
            'operation_name',
            'machine_id',
            'part_id',
            'batch_number',
            'quantity'
        ]
        widgets = {
            'master': forms.Select(attrs={'class': 'form-control'}),
            'operator': forms.Select(attrs={'class': 'form-control'}),
            'operation_name': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Введите наименование операции'}),
            'machine_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер станка'}),
            'part_id': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите наименование детали'}),
            'batch_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Введите номер партии'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Введите количество'}),
        }

    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        if quantity < 0:
            raise forms.ValidationError("Количество не может быть отрицательным.")
        return quantity
