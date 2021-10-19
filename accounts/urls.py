from django.contrib import admin
from django.urls import include, path
from accounts import views

app_name = 'accounts'

urlpatterns = [
    path('home/', views.ProfileView.as_view(), name=''),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('profile/edit', views.ProfileEditView.as_view(), name='profile_edit'),
]

