from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from users.models import User
from django.utils.translation import gettext_lazy as _


class StyleFormMixin:
    """
    Миксин для стилизации форм.

    Этот миксин добавляет класс 'form-control' ко всем полям формы,
    чтобы применить стили Bootstrap.
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class UserForm(StyleFormMixin, forms.ModelForm):
    """
    Форма для создания или редактирования пользователя.

    Эта форма используется для ввода данных о пользователе,
    включая имя пользователя, имя и фамилию.
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'role',)


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    """
    Форма для регистрации нового пользователя.

    Эта форма используется для создания нового пользователя с проверкой пароля.
    """

    class Meta:
        model = User
        fields = ('username',)

    def clean_password2(self):
        """
        Проверка соответствия паролей.

        Если введенные пароли не совпадают, выбрасывает ValidationError.
        """
        temp_data = self.cleaned_data
        if temp_data['password1'] != temp_data['password2']:
            raise forms.ValidationError('password_mismatch')
        return temp_data['password2']


class UserLoginForm(AuthenticationForm):
    """
    Форма для аутентификации пользователя.

    Эта форма проверяет правильность введенных имени пользователя и пароля.
    """

    def clean(self):
        """Проверяет наличие ошибок в форме и генерирует сообщение об ошибке."""
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
    """
    Форма для обновления данных пользователя.

    Эта форма используется для редактирования информации о пользователе.
    """

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name',)


