
  
import re
from django import forms
from django.db import models
from django.db.models import Q
from django.db.models.query_utils import select_related_descend
from django.forms import formset_factory
from django.forms.models import inlineformset_factory
from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.generic import View, TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from rest_framework import views as RestApiViews
from rest_framework.response import Response
from .models import Post, Object, UploadFile
from .serializers import PostsIndexSerializer, PostDetailSerializer 
from .forms import PostForm, ObjectForm, ObjectCreateForm, SamplePostForm, ObjectCreateModel, UploadFileForm
from scraype.scrayping import find_folders, search_url_text
from functools import reduce
from operator import and_, le, pos
from urllib.parse import urlencode
# Create your views here.


'''

Restful API

'''

class ArticleIndexAPIView(RestApiViews.APIView):

    def get(self, request, format=None):
        posts = Post.objects.all()
        serializer = PostsIndexSerializer(posts, many=True)
        return Response(serializer.data)
        return Response(serializer.data)


'''
トップ画面用view
'''
class IndexView(ListView):
    
    model = Post
    queryset = Post.objects.filter(status = True).order_by('-id')
    context_object_name = "post_list"
    template_name = "articles/index.html"

'''
利用規約ページ
'''
class TermsView(TemplateView):
    template_name = 'terms.html'

'''
プライバシーポリシーページ
'''
class PrivacyPolicyView(TemplateView):
    template_name = 'privacy_policy.html'

'''
詳細画面用のView
クラス汎用ベースビューのDetailViewを継承して作っている
'''

class ArticleDetailView(DetailView):
    model = Post
    template_name = "articles/detail.html"
    # Should match the value after ':' from url <slug:slug>
    slug_url_kwarg = 'slug'
    # Should match the name of the slug field on the model 
    slug_field = 'slug' # DetailView's default value: optional


#Post単体を新規作成するクラス
class CreatePostView(LoginRequiredMixin, View):
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
class CreateObjectView(LoginRequiredMixin, CreateView):
    model = Object
    form_class = ObjectForm
    template_name = "articles/create_object.html"
    success_url = "/"


"""
PostやObjectを同時に新規作成・編集するクラス
今回はinlineformsetという機能を使用している
"""

"""
PostとObjectを新規作成するクラス
"""

class CreatePostObjectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = PostForm(request.POST or None)
        formset = ObjectCreateForm()

        return render(request, 'articles/new_postobj.html', {
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

            formset = ObjectCreateForm(request.POST, instance = post)

            if formset.is_valid():
                post.save()
                formset.save()
                return redirect('/')
            
            else:
                return render(request, 'articles/new_postobj.html', {
                    'form':form,
                    'formset':formset,
                })

"""
PostとObjectを編集（アップデート）するクラス
"""

class UpdatePostObjectView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        if request.user != post_data.user:
            messages.error(request, "あなたにはそのページへのアクセス権限がありません")
            return redirect('index')
        else:
            form = PostForm(request.POST or None,
            initial = {
                'title':post_data.title,
                'discription':post_data.discription,
                'status':post_data.status,
            })

            formset = ObjectCreateForm(instance=post_data)

            return render(request, 'articles/new_postobj.html', {
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
                    return render(request, 'articles/new_postobj.html', {
                        'form':form,
                        'formset':formset,
                    })
### ブックマークファイルアップロード ####
                    
class FileUploadView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = UploadFileForm()

        return render(request, 'articles/file_upload.html', {'form':form})
    
    def post(self, request, *args, **kwargs):
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = UploadFile()
            file.user = request.user
            file.bukuma_file = form.cleaned_data['bukuma_file']
            file.save()
            return redirect('select_folder')
        else:
            return render(request, 'articles/file_upload.html', {'form':form})

class SelectFolderView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        url = UploadFile.objects.filter(user=request.user).order_by('id').last()
        folders = find_folders(url.bukuma_file)
        return render(request, 'articles/select_folder.html', {'folders':folders})

    def post(self, request, *args, **kwargs):
        check = request.POST['select_folder']
        redirect_url = reverse('file_edit')
        parameters = urlencode({'param1':check})
        url = f'{redirect_url}?{parameters}'
        return redirect(url)
        
        # url = UploadFile.objects.filter(user=request.user).order_by('id').last()
        # contents = search_url_text(url.bukuma_file,check)
        # formset = ObjectCreateForm(initial=contents)
        # return render(request, 'articles/select_folder.html',{'contents':contents, 'formset':formset})

class FileEditView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        check = request.GET['param1']
        url = UploadFile.objects.filter(user=request.user).order_by('id').last()
        contents = search_url_text(url.bukuma_file,check)
        FileEditForm = inlineformset_factory(
           Post, Object, form=ObjectForm, extra=len(contents), can_delete=True
        )
        form = PostForm()
        formset = FileEditForm(initial = contents)
        return render(request, 'articles/new_postobj.html', {'form':form, 'formset':formset})
    
    def post(self, request, *args, **kwargs):
        check = request.GET['param1']
        url = UploadFile.objects.filter(user=request.user).order_by('id').last()
        contents = search_url_text(url.bukuma_file,check)
        FileEditForm = inlineformset_factory(
        Post, Object, form=ObjectForm, extra=len(contents), can_delete=True
        )
        form = PostForm(request.POST or None)
        
        

        if form.is_valid():
            post = Post()
            post.user = request.user
            post.title = form.cleaned_data['title']
            post.discription = form.cleaned_data['discription']
            post.status = form.cleaned_data['status']
            
            formset = FileEditForm(request.POST or None, instance=post, initial = contents)
            if formset.is_valid():
                post.save()
                for file in formset:
                    file.has_changed()
                    file.save()
                return redirect('index')
            else:
                form = PostForm(request.POST or None)
                formset = FileEditForm(initial = contents)
                return render(request, 'articles/new_postobj.html', {'form':form, 'formset':formset})


class SearchView(View):
    def get(self, request, *args, **kwargs):
        post_list = Post.objects.filter(status=True).order_by('-id')
        keyword = request.GET.get('keyword')

        if keyword:
            exclusion = set([' ','　'])
            query_list = ''

            for word in keyword:
                if not word in exclusion:
                    query_list += word
            if len(query_list) == 0:
                return redirect('index')
            query = reduce(and_, [Q(title__icontains=q)|Q(discription__icontains=q) for q in query_list])
            post_list = post_list.filter(query)
            count_post = len(post_list)

            return render(request, 'articles/index.html', {
                'post_list':post_list,
                'keyword':keyword,
                'count_post':count_post
            })
        else:
            return redirect('index')

#削除機能　編集画面以外で削除機能を使う場合に使用
@method_decorator(require_POST, name='dispatch')
class ArticleDeleteView(View, LoginRequiredMixin):
    def post(self, request, *args, **kwargs):
        post_data = Post.objects.get(id=self.kwargs['pk'])
        if request.user == post_data.user:
            post_data.delete()
            return redirect('index')
        else:
            messages.error(request, "あなたにはそのページの編集権限がありません")
            redirect('article_detail', pk=post_data.id)






