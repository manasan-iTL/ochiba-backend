from django import views
from django.core.validators import slug_re
from django.shortcuts import render, redirect

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls.base import reverse  # 追加
from django.views.generic import CreateView, TemplateView, DetailView, UpdateView

from .forms import ProfileEditForm, SignupForm
from .models import CustomUser
from django.views import View
from allauth.account.views import LoginView, LogoutView, SignupView
from articles.models import Post, Object

class ProfileView(View):
    slug_field = 'username'
    slug_url_kwarg = 'username'
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(username=self.kwargs['username'])
        post_data = Post.objects.filter(user=user_data,status=True).all
        post_unpub_data = Post.objects.filter(user=user_data, status=False).all

        return render(request, 'accounts/profile.html', {
            'user_data': user_data,
            'post_data': post_data,
            'post_unpub_data': post_unpub_data,
        })

class ProfileEditView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        user_data = CustomUser.objects.get(id=request.user.id)
        form = ProfileEditForm(
            request.POST or None,
            initial={
                'first_name': user_data.first_name,
                'last_name': user_data.last_name,
                'description': user_data.description,
                'image': user_data.image
            }
        )

        return render(request, 'accounts/profile_edit.html', {
            'form': form,
            'user_data': user_data
        })

    def post(self, request, *args, **kwargs):
        form = ProfileEditForm(request.POST or None)
        if form.is_valid():
            user_data = CustomUser.objects.get(id=request.user.id)
            user_data.first_name = form.cleaned_data['first_name']
            user_data.last_name = form.cleaned_data['last_name']
            user_data.description = form.cleaned_data['description']
            if request.FILES.get('image'):
                user_data.image = request.FILES.get('image')
            user_data.save()
            return redirect('accounts:profile', request.user)

        return render(request, 'accounts/profile.html', {
            'form': form
        })


# class LoginView(LoginView):
#     template_name = 'account/login.html'

# class LogoutView(LogoutView):
#     template_name = 'account/logout.html'

# class SignupView(SignupView):
#     template_name = 'account/logout.html'
#     form_class = SignupForm