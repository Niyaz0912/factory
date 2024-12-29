from django import forms

from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django.utils.translation import gettext_lazy as _


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'role',)


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        temp_data = self.cleaned_data
        if temp_data['password1'] != temp_data['password2']:
            raise forms.ValidationError('password_mismatch')
        return temp_data['password2']


class UserLoginForm(AuthenticationForm):
    def clean(self):
        super().clean()
        if self.errors:
            error_messages = []
            for field in self.errors:
                error_messages.extend(self.errors[field])
            if error_messages:
                raise forms.ValidationError(_('Пожалуйста, введите правильные имя пользователя и пароль. '
                                              'Оба поля могут быть чувствительны к регистру.'))

        return self.cleaned_data


class UserUpdateForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'role',)

