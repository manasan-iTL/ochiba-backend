
  
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post
# Create your views here.

class IndexView(ListView):
    
    model = Post
    queryset = Post.objects.all()
    context_object_name = "post_list"
    template_name = "articles/index.html"

class ArticleListView(LoginRequiredMixin, ListView):
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin, DetailView):
    template_name = "article_detail.html"

class ArticleCreateView(LoginRequiredMixin, CreateView):
    template_name = "article_create.html"

class ArticleUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'article_update.html'

class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    template_name = "article_delete.html"

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'users/edit.html'

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'

