from django.db.models import fields
from django.forms.fields import FileField
from django.forms.widgets import TextInput, Textarea, URLInput, Widget

from accounts.models import CustomUser
from .models import Object, Post, UploadFile
from django import forms
from django.db.models.base import Model
from django.db.models.fields import CharField


from django.core.exceptions import ValidationError #add
from django.core.validators import FileExtensionValidator, validate_email #add

class PostForm(forms.Form):
    title = forms.CharField(max_length=100, label='記事タイトル', required=True, widget = forms.TextInput(attrs={'placeholder':'ブックマークリストタイトル'}))
    discription = forms.CharField(label='記事の概要', widget=forms.Textarea(attrs={'placeholder':'このブックマークリストについて'}))
    status = forms.BooleanField(label='公開する', required=False)

class ObjectForm(forms.ModelForm):
    class Meta:
        model = Object
        fields = ('url','title', 'discription', 'post_data')
        widgets = {
            'url':URLInput(attrs={'placeholder':'ブックマークした記事のURLを入力'}),
            'title':TextInput(attrs={'placeholder':'ブックマークした記事のタイトルを入力'}),
            'discription':Textarea(attrs={'placeholder':'ブックマークした記事の概要、メモを入力'}),
        }

class UploadFileForm(forms.Form):
    bukuma_file = FileField(label="HTMLファイル",
    required=True,
    validators=[FileExtensionValidator(['html',])],
    widget=forms.widgets.FileInput)

# インラインフォームの記述

ObjectCreateForm = forms.inlineformset_factory(
    Post, Object, form=ObjectForm, 
    extra=2, can_delete=True
)



### ここから下はテスト用　使っていないため後々消す予定　######

# テスト用のモデルフォーム
class SamplePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'discription', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'placefolder':'ブックマークしたページのタイトルを入力'}),
            'discription': forms.Textarea(attrs={'placefolder':'ブックマークしたサイトの説明やメモを入力'}),
        }

#テスト用インラインフォーム
ObjectCreateModel = forms.modelformset_factory(
    Object, exclude=('post_data',), 
    extra=2, can_delete= True
)

class ProfileEditForm(forms.ModelForm):
    name = forms.CharField(max_length=50, required=True, widget=forms.TextInput(attrs={'placeholder': "ユーザー名"}),)
    email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': "メールアドレス"}),)
    username = forms.CharField(max_length=50, widget=forms.TimeInput(attrs={'placeholder': "ユーザーID"}),)
    about_me = forms.CharField(widget=forms.Textarea(attrs={'size': 50}),)

    class Meta:
        model = CustomUser
        fields = ('name', 'email', 'username', 'about_me',)

    def __init__(self, *args, **kwargs):
        self.user = kwargs.get('instance', None)
        super().__init__(*args, **kwargs)

    def clean_email(self):
        email = self.cleaned_data["email"]

        try:
            validate_email(email)
        except ValidationError:
            raise ValidationError("正しいメールアドレスを指定してください")

        try:
            user = CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            return email
        else:
            if self.user.email == email:
                return email

            raise ValidationError("このメールアドレスは既に使用されています")