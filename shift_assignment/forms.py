from django import forms
from django.core.exceptions import ValidationError

from users.forms import StyleFormMixin
from shift_assignment.models import ShiftAssignment, CompletedShiftAssignment


class ShiftAssignmentForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания или редактирования сменного задания.

    Эта форма используется для ввода данных о сменном задании, включая
    номер партии, наименование операции, количество, оператора и идентификатор машины.
    """

    class Meta:
        model = ShiftAssignment  # Модель, с которой работает форма
        fields = ['batch_number', 'operation_name', 'quantity', 'operator', 'part_id', 'machine_id']


class CompletedShiftAssignmentForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания или редактирования завершенного сменного задания.

    Эта форма используется для ввода данных о завершенном сменном задании,
    включая количество брака и причину остановки.
    """

    # Поле для ввода количества брака (необязательное)
    defect_quantity = forms.IntegerField(required=False, label='Количество брака', initial=0)

    # Поле для выбора причины остановки процесса
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
        model = CompletedShiftAssignment  # Модель, с которой работает форма
        fields = [
            # 'date',  # Если нужно добавить поле даты, раскомментируйте
            'operator',
            'operation_name',
            'machine_id',
            'part_id',
            'batch_number',
            'quantity',
            'defect_quantity',
            'stop_reason'
        ]
        widgets = {
            # Кастомизация виджетов для полей формы
            'date': forms.DateInput(attrs={'type': 'date'}),
            'quantity': forms.NumberInput(attrs={'min': 1, 'placeholder': 'Введите количество'}),
            # Добавьте другие кастомные виджеты по необходимости
        }

    def clean_quantity(self):
        """
        Валидация поля quantity.

        Проверяет, что количество больше нуля. Если значение некорректно,
        выбрасывает ValidationError.
        """
        quantity = self.cleaned_data.get('quantity')

        if quantity is not None and quantity <= 0:
            raise ValidationError("Количество должно быть больше нуля.")

        return quantity
