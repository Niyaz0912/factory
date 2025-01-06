from django import forms
from django.core.exceptions import ValidationError

from users.forms import StyleFormMixin
from shift_assignment.models import ShiftAssignment, CompletedShiftAssignment


class ShiftAssignmentForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = ShiftAssignment
        fields = ['batch_number', 'operation_name', 'quantity', 'operator', 'part_id', 'machine_id']


class CompletedShiftAssignmentForm(StyleFormMixin, forms.ModelForm):
    defect_quantity = forms.IntegerField(required=False, label='Количество брака')
    stop_reason = forms.ChoiceField(
        choices=[
            ('Работа в нормальном режиме', 'Работа в нормальном режиме'),
            ('СлНал', 'СлНал'),
            ('ТОиР', 'ТОиР'),
            ('Прочее', 'Прочее'),
        ],
        label='Причина остановки'
    )

    class Meta:
        model = CompletedShiftAssignment
        fields = [
            'operator',
            'operation_name',
            'machine_id',
            'part_id',
            'batch_number',
            'quantity',
            'defect_quantity',  # Добавляем поле количества брака
            'stop_reason'       # Добавляем поле причины остановки
        ]
        widgets = {
            # Применяем виджеты для улучшения отображения полей
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_quantity(self):
        """Валидация поля quantity."""
        quantity = self.cleaned_data.get('quantity')
        if quantity is not None and quantity <= 0:
            raise ValidationError("Количество должно быть больше нуля.")
        return quantity

