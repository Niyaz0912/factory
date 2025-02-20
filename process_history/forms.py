from django import forms
from django.core.exceptions import ValidationError
from process_history.models import ProcessHistory
from shift_assignment.models import ShiftAssignment
from users.forms import StyleFormMixin


class ProcessHistoryForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для ввода данных о процессе.

    Эта форма используется для создания или редактирования записей
    в модели ProcessHistory. Она включает поля для проверки
    различных характеристик процесса.
    """

    # Поле для ввода количества брака (необязательное)
    defect_quantity = forms.IntegerField(required=False, label='Количество брака')

    # Поле для выбора причины остановки процесса
    stop_reason = forms.ChoiceField(
        choices=[
            ('СлНал', 'СлНал'),
            ('ТОиР', 'ТОиР'),
            ('Прочее', 'Прочее'),
        ],
        label='Причина остановки'
    )

    # Поле для ввода специальных характеристик
    special_characteristics = forms.DecimalField(
        label='Специальные характеристики',
        max_digits=5,
        decimal_places=3,
        required=False
    )

    class Meta:
        model = ProcessHistory  # Модель, с которой работает форма
        fields = [
            'roughness_check',
            'defects_check',
            'threading_check',
            'diameter_check',
            'value',
            'detail_quantity',
            'control_code',
            'mark_yes_no',
            'defect_quantity',  # Добавляем поле количества брака
            'stop_reason',  # Добавляем поле причины остановки
            'special_characteristics'  # Добавляем поле специальных характеристик
        ]

    def clean_value(self):
        """
        Валидация поля value.

        Проверяет, что значение находится в заданном диапазоне и округляет его до трех знаков после запятой.
        """
        value = self.cleaned_data.get('value')

        if value is not None:
            # Проверка диапазона
            if not (21.95 <= value <= 22):
                raise ValidationError('Значение должно быть в диапазоне от 21.95 до 22.')

            # Округление до трех знаков после запятой
            return round(value, 3)

        return value


class QualityControlForm(StyleFormMixin, forms.Form):
    """
    Форма для контроля качества.

    Эта форма используется для ввода данных о шероховатости и отсутствии дефектов.
    """

    roughness = forms.DecimalField(label='Шероховатость (мкм)', max_digits=5, decimal_places=2)

    defects_absent = forms.BooleanField(required=False, label='Отсутствие рисок, канавок и т.д.')


class SaveProcessHistoryForm(StyleFormMixin, forms.ModelForm):
    """Форма для сохранения истории процесса."""

    class Meta:
        model = ShiftAssignment  # Укажите модель, с которой работаете
        fields = [
            'operator',
            'master',
            'operation_name',
            'machine_id',
            'part_id',
            'batch_number',
            'quantity',
            'file'
        ]

        widgets = {
            # Применяем виджеты для улучшения отображения полей
            'date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_quantity(self):
        """
        Валидация поля quantity.

        Проверяет, что количество больше нуля.
        """
        quantity = self.cleaned_data.get('quantity')

        if quantity <= 0:
            raise forms.ValidationError("Количество должно быть больше нуля.")

        return quantity

