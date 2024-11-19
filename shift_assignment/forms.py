from django import forms
from shift_assignment.models import ShiftAssignment


class ShiftAssignmentForm(forms.ModelForm):
    file = forms.FileField(label='Выбрать файл .xls', required=False)  # Добавлено поле для загрузки файла

    class Meta:
        model = ShiftAssignment
        fields = [
            'operator',
            'operation_name',
            'machine_id',
            'part_id',
            'batch_number',
            'quantity',
            'file'
        ]
        widgets = {
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

