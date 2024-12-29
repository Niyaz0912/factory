from django import forms
from django.views.generic import CreateView

from process_history.models import ProcessHistory


class ProcessHistoryForm(forms.ModelForm):
    class Meta:
        model = ProcessHistory
        fields = ['roughness_check', 'defects_check', 'threading_check', 'diameter_check', 'value', 'detail_quantity',
                  'control_code', 'mark_yes_no']


class QualityControlForm(forms.Form):
    roughness = forms.DecimalField(label='Шероховатость (мкм)', max_digits=5, decimal_places=2)
    defects_absent = forms.BooleanField(required=False, label='Отсутствие рисок, канавок и т.д.')


class HistoryProcessCreateView(CreateView):
    model = ProcessHistory
    form_class = ProcessHistoryForm  # Используйте свою форму
    template_name = 'process_history/history_process_create.html'
    success_url = '/success/'  # Укажите URL для перенаправления после успешного создания
