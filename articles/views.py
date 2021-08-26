from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = "index.html"

class ArticleListView(LoginRequiredMixin, generic.ListView):
    template_name = "article_list.html"

class ArticleDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = "article_detail.html"

class ArticleCreateView(LoginRequiredMixin, generic.CreateView):
    template_name = "article_create.html"

class ArticleUpdateView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'article_update.html'

class ArticleDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = "article_delete.html"

class ProfileEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'users/edit.html'

class ProfileDetailView(LoginRequiredMixin, generic.DetailView):
    template_name = 'users/detail.html'

