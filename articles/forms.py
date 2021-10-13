from django.db.models import fields
from django.forms import widgets
from django.forms.widgets import TextInput, Textarea, URLInput, Widget
from .models import Object, Post
from django import forms
from django.db.models.base import Model
from django.db.models.fields import CharField

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

# テスト用のモデルフォーム

class SamplePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'discription', 'status')
        widgets = {
            'title': forms.TextInput(attrs={'placefolder':'ブックマークしたページのタイトルを入力'}),
            'discription': forms.Textarea(attrs={'placefolder':'ブックマークしたサイトの説明やメモを入力'}),
        }

# テスト用インラインフォームの記述

ObjectCreateForm = forms.inlineformset_factory(
    Post, Object, form=ObjectForm, 
    extra=2, can_delete=True
)

ObjectCreateModel = forms.modelformset_factory(
    Object, exclude=('post_data',), 
    extra=2, can_delete= True
)