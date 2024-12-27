from django import forms
from django.views.generic import CreateView

from process_history.models import ProcessHistory


class ProcessHistoryForm(forms.ModelForm):
    class Meta:
        model = ProcessHistory
        fields = ['control_code', 'mark', 'quantity', 'parameters']


class HistoryProcessCreateView(CreateView):
    model = ProcessHistory
    form_class = ProcessHistoryForm  # Используйте свою форму
    template_name = 'process_history/history_process_create.html'
    success_url = '/success/'  # Укажите URL для перенаправления после успешного создания
