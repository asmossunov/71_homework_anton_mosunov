from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model



from accounts.models import Gender


class LoginForm(forms.Form):
    email = forms.CharField(required=True, label='Логин')
    password = forms.CharField(required=True, label='Пароль', widget=forms.PasswordInput)
    next = forms.CharField(required=False, widget=forms.HiddenInput)


class CustomUserCreationForm(forms.ModelForm):
    username = forms.CharField(label='Логин')
    password = forms.CharField(label='Пароль', strip=False, required=True, widget=forms.PasswordInput)
    password_confirm = forms.CharField(label='Подтвердите пароль', strip=False, required=True, widget=forms.PasswordInput)
    phone = forms.CharField(label='Номер телефона')
    first_name = forms.CharField(label='Имя')
    gender = forms.ModelChoiceField(
        label='Пол',
        queryset=Gender.objects.all(),

    )


    class Meta:
        model = get_user_model()
        fields = ('username',  'email', 'avatar', 'password', 'password_confirm',
                  'first_name', 'about_user', 'phone', 'gender')

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get('password')
            password_confirm = cleaned_data.get('password_confirm')
            if password and password_confirm and password != password_confirm:
                raise ValidationError('Пароли не совпадают')

        def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data.get('password'))
            user.groups.add('user')

            if commit:
                user.save()
            return user


class UserChangeForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'email', 'avatar', 'birthday', 'first_name',
                  'last_name', 'about_user', 'phone', 'gender',)
        labels = {'first_name': 'Имя', 'last_name': 'Фамилия', 'email': 'Email'}
