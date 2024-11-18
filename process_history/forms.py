from django import forms
from process_history.models import ProcessHistory


class ProcessHistoryForm(forms.ModelForm):
    class Meta:
        model = ProcessHistory
        fields = "__all__"


class ProcessHistoryFormShort(forms.ModelForm):
    class Meta:
        model = ProcessHistory
        exclude = ("param3", "param4", "param5")



