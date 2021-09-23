from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, SET_NULL
from django.db.models.fields import CharField
# Create your models here.

class Post(models.Model):
    title = models.CharField("タイトル", max_length=100, blank=False, null=False)
    discription = models.TextField("概要", blank=True, null=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, blank=False, null=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, blank=False, null=False)
    status = models.BooleanField(default=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Object(models.Model):
    url = models.URLField()
    title = models.CharField("タイトル", max_length=100, blank=False, null=False)
    discription = models.TextField("概要", blank=True, null=True)
    post_data = models.ForeignKey(Post, null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.title