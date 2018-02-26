from django import forms

from .models import UserData


class SignUpForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': 'Укажите Login'})
    password = forms.CharField(required=True, error_messages={'required': 'Укажите пароль'})
    confirm_password = forms.CharField(required=True, error_messages={'required': 'Повторите пароль'})

    def clean(self):

        username = str(self.cleaned_data.get('username'))

        print(username)

        # Проверка совпадения имени
        username_is_busy = False
        try:
            user = UserData.objects.get(username=username)
            username_is_busy = True
        except:
            pass
        if username_is_busy:
            raise forms.ValidationError('Этот Username занят!')

        return self.cleaned_data


class SignInForm(forms.Form):
    username = forms.CharField(required=True, error_messages={'required': 'Укажите Username'})
    password = forms.CharField(required=True, error_messages={'required': 'Укажите пароль'})

    def clean(self):

        username = str(self.cleaned_data.get('username'))
        password = str(self.cleaned_data.get('password'))

        try:
            user = UserData.objects.get(username=username)
        except:
            raise forms.ValidationError('Не правильный Username!')

        if(user.password not in password):
            raise forms.ValidationError('Не правильный пароль!')

        return self.cleaned_data