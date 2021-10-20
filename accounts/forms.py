from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from allauth.account.forms import SignupForm
from django.forms.fields import CharField
from django.http import request
from .models import CustomUser
from PIL import Image


# class CustomUserCreationForm(UserCreationForm):
#   class Meta(UserCreationForm):
#       model = CustomUser
#       fields = UserCreationForm.Meta.fields + ('age','favorite_celebrity')

# class CustomUserChangeForm(UserChangeForm):
#   class Meta:
#     model = CustomUser
#     fields = UserChangeForm.Meta.fields



# class ProfileEditForm(forms.ModelForm):
#     name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': "ユーザー名"}),)
#     email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': "メールアドレス"}),)
#     username = forms.CharField(max_length=50, widget=forms.TimeInput(attrs={'placeholder': "ユーザーID"}),)

    # class Meta:
    #     model = CustomUser
    #     fields = ('name', 'email', 'username', 'about_me',)

    # def __init__(self, *args, **kwargs):
    #     self.user = kwargs.get('instance', None)
    #     super().__init__(*args, **kwargs)

    # def clean_email(self):
    #     email = self.cleaned_data["email"]

    #     try:
    #         validate_email(email)
    #     except ValidationError:
    #         raise ValidationError("正しいメールアドレスを指定してください")

    #     try:
    #         user = User.objects.get(email=email)
    #     except User.DoesNotExist:
    #         return email
    #     else:
    #         if self.user.email == email:
    #             return email

    #         raise ValidationError("このメールアドレスは既に使用されています")

class ProfileEditForm(forms.Form):
    first_name = forms.CharField(max_length=30, label='姓')
    last_name = forms.CharField(max_length=30, label='名')
    description = forms.CharField(label='自己紹介', widget=forms.Textarea(), required=False)
    image = forms.ImageField(required=False)

class SignupForm(SignupForm):
  first_name = forms.CharField(max_length=30, label='姓')
  last_name = forms.CharField(max_length=30, label='名')

  def save(self, request):
    user = super(SignupForm, self).save(request)
    user.first_name = self.cleaned_data['first_name']
    user.last_name = self.cleaned_data['last_name']
    return user