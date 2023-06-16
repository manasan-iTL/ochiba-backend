from re import DEBUG
from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField
from django.utils import html
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
# Create your models here.

class Post(models.Model):
    title = models.CharField("タイトル", max_length=100, blank=False, null=False)
    discription = models.TextField("概要", blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=False, null=False)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.user.username)
        return super(Post,self).save(*args, **kwargs)

class Object(models.Model):
    url = models.URLField(max_length=400)
    title = models.CharField("タイトル", max_length=100, blank=False, null=False)
    discription = models.TextField("概要", blank=True, null=True)
    post_data = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL, related_name="post")

    def __str__(self):
        return self.title

class UploadFile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bukuma_file = models.FileField(
        upload_to='files/html',
        verbose_name='ブックマークファイル',
        validators=[FileExtensionValidator(['html',])],
        )
