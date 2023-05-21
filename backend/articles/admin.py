from django.contrib import admin
from .models import Object, Post, UploadFile

# Register your models here.
admin.site.register(Object)
admin.site.register(Post)
admin.site.register(UploadFile)


