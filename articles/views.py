  
from django.db import models
from django.db.models.query import QuerySet
from django.forms import formsets
from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from .models import Post, Object
from .forms import PostForm, ObjectForm, ObjectCreateForm, SamplePostForm, ObjectCreateModel
# Create your views here.


#トップ画面用view
class IndexView(ListView):
    
    model = Post
    queryset = Post.objects.filter(status = True).all()
    context_object_name = "post_list"
    template_name = "articles/index.html"


#詳細画面用のView
class ArticleDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "articles/detail.html"

"""
PostやObjectを同時に新規作成・編集するクラス
今回はinlineformsetという機能を試用している
"""

"""
PostとObjectを新規作成するクラス
"""
class SampleCreateObjectView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        formset = ObjectCreateForm()

        return render(request, 'articles/test.html', {
            'form':form,
            'formset': formset,
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():

            post = Post()
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.discription = form.cleaned_data['discription']
            post.status = form.cleaned_data['status']

            formset = ObjectCreateForm(request.POST, instance=post)

            if formset.is_valid():
                post.save()
                formset.save()
                return redirect('/')
            
            else:
                return render(request, 'articles/test.html', {
                    'form':form,
                    'formset':formset,
                })

"""
PostとObjectを編集（アップデート）するクラス
"""
class SampleUpdateObjectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(request.POST or None,
        initial = {
            'title':post_data.title,
            'discription':post_data.discription,
            'status':post_data.status,
        })

        formset = ObjectCreateForm(instance=post_data)

        return render(request, 'articles/test.html', {
            'form':form,
            'formset': formset,
        })
    
    def post(self, request, *args, **kwargs):

        post_data = Post.objects.get(id=self.kwargs['pk'])
        if 'postdelete' in request.POST:
            post_data.delete()

            return redirect('index')
        
        elif 'save' in request.POST:
            form = PostForm(request.POST or None)

            if form.is_valid():

                post = Post.objects.get(id=self.kwargs['pk'])
                post.user = request.user
                post.title = form.cleaned_data['title']
                post.discription = form.cleaned_data['discription']
                post.status = form.cleaned_data['status']

                formset = ObjectCreateForm(request.POST, instance=post_data)

                if formset.is_valid():
                    post.save()
                    formset.save()
                    return redirect('/')
            
                else:
                    return render(request, 'articles/test.html', {
                        'form':form,
                        'formset':formset,
                    })

"""
ここから下は今の段階では使っていないが、使うかもしれない機能を実装してある。
最終的に使わない場合はデプロイ前に削除ないしコメントアウトする
"""

#Post単体を新規作成するクラス
class CreatePostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        return render(request, "articles/create_post.html", {
            'form' : form
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post_data = Post()
            post_data.user = request.user
            post_data.title = form.cleaned_data['title']
            post_data.discription = form.cleaned_data['discription']
            post_data.status = form.cleaned_data['status']
            post_data.save()
            return redirect('/')

#Object単体を新規作成するクラス
class CreateObjectView(CreateView):
    model = Object
    form_class = ObjectForm
    template_name = "articles/create_object.html"
    success_url = "/"

#Modelformsetによる実装　今回はinlineformsetでの実装を採用しているがこの方法でもおそらくできる
class CreateObjectPostView(View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        formset = ObjectCreateModel(request.POST or None, queryset=Object.objects.none())
        return render(request, 'articles/test2.html', {
            'form':form,
            'formset':formset,
        })
    
    def post(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)

        if form.is_valid():
            post = Post()
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.discription = form.cleaned_data['discription']
            post.status = form.cleaned_data['status']

            formset = ObjectCreateModel(request.POST or None, queryset=Object.objects.none())

            if formset.is_valid():
                post.save()
                objects = formset.save(commit=False)

                for file in formset.deleted_objects:
                    file.delete()
                
                for file in objects:
                    file.post_data = post
                    file.save()
                return redirect('/')
                
            else:
                return render(request, 'articles/test2.html', {
                    'form':form,
                    'formset':formset,
                })

class ArticleUpdateView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        form = PostForm(
            request.POST or None, 
            initial = {
                'title':post_data.title,
                'discription':post_data.discription,
                'status':post_data.status,
            })
        formset = ObjectCreateModel(request.POST or None, queryset=Object.objects.filter(post_data__id = post_data.id))

        return render(request, 'articles/postedit.html', {
            'form': form,
            'formset': formset,
        })
    
    def post(self, request, *args, **kwargs):

        form = PostForm(request.POST or None)

        if form.is_valid():
            post = Post.objects.get(id=self.kwargs['pk'])
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.discription = form.cleaned_data['discription']
            post.status = form.cleaned_data['status']

            formset = ObjectCreateModel(request.POST or None, queryset=Object.objects.filter(post_data__id = post.id))
            
            if formset.is_valid():
                post.save()
                objects = formset.save(commit=False)

                for file in formset.deleted_objects:
                    file.delete()
                
                for file in objects:
                    file.post_data = post
                    file.save()

                return redirect('article_detail', self.kwargs['pk'])
            
            return render(request, 'articles/postedit.html', {
                'form': form,
                'formset': formset,
            })

#削除機能　編集画面以外で削除機能を使う場合に使用
@method_decorator(require_POST, name='dispatch')
class ArticleDeleteView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        post_data.delete()
        return redirect('index')

class ProfileEditView(LoginRequiredMixin, UpdateView):
    template_name = 'users/edit.html'

class ProfileDetailView(LoginRequiredMixin, DetailView):
    template_name = 'users/detail.html'