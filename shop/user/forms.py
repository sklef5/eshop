from django import forms
from django.contrib.auth import authenticate
from django.core.validators import MinValueValidator, ValidationError
from user.models import UserModel


class SignUpForm(forms.Form):
    username = forms.CharField(max_length=15, label='Логін')
    email = forms.EmailField(label='E-mail', required=False)
    password1 = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Пароль')
    password2 = forms.CharField(max_length=15, widget=forms.PasswordInput, label='Повторить пароль')
    first_name = forms.CharField(max_length=20, required=False, label="Им'я")
    last_name = forms.CharField(max_length=50, label='Прізвище')
    age = forms.IntegerField(validators=[MinValueValidator(10)], label='Рік')

    def clean_username(self):
        username = self.cleaned_data["username"]
        try:
            UserModel.objects.get(username=username)
            raise ValidationError("Логін вже зайнятий")
        except UserModel.DoesNotExist:
            return username

    def clean(self):
        password1 = self.cleaned_data["password1"]
        password2 = self.cleaned_data["password2"]
        if password1 != password2:
            raise ValidationError("Паролі не співпадають")

    def create_user(self):
        username = self.cleaned_data["username"]
        email = self.cleaned_data["email"]
        password = self.cleaned_data["password1"]
        first_name = self.cleaned_data["first_name"]
        last_name = self.cleaned_data["last_name"]
        age = self.cleaned_data["age"]
        UserModel.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name, age=age)



class UpdateNameForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['first_name', 'last_name']


class UpdateLogForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ["username"]