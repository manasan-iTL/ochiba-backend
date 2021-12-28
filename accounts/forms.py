from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.core import validators
from django.core.validators import RegexValidator, slug_re
from django.db.models.base import Model
from allauth.account.forms import SignupForm
from django.forms.fields import CharField
from django.http import request
from .models import CustomUser

class ProfileEditForm(forms.Form):
    username = forms.CharField(max_length=30, 
    label='ユーザー名', 
    validators=[RegexValidator(slug_re,'名前には半角英数字、アンダーバー、ハイフンのみ指定できます。')],
    widget=forms.TextInput(attrs={'pattern':'^[A-Za-z0-9_-]+$'}))
    # password = forms.CharField(max_length=30, label='パスワード') 出したらエラーが出る
    first_name = forms.CharField(max_length=30, label='姓', required=False)
    last_name = forms.CharField(max_length=30, label='名', required=False)
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False)

# class ProfileEditForm(forms.ModelForm):
#   class Meta:
#     model = CustomUser


class SignupForm(SignupForm):
  first_name = forms.CharField(max_length=30, label='姓')
  last_name = forms.CharField(max_length=30, label='名')

  def save(self, request):
    user = super(SignupForm, self).save(request)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    return user