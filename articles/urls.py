from django.urls import path
from articles import views


#app_name = 'diary'


urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    # path('article-detail/<int:pk>/', views.ArticleDetailView.as_view(), name="article_detail"),
    path('<slug:slug>/<int:pk>', views.ArticleDetailView.as_view(), name="article_detail"),
    path('create-post/', views.CreatePostView.as_view(), name="create_post"),
    path('create-object/', views.CreateObjectView.as_view(), name="create_object"),
    path('test/', views.SampleCreateObjectView.as_view(), name="test"),
    path('article-post/<int:pk>/newupdate', views.SampleUpdateObjectView.as_view(), name="object_update"),
    path('article-delete/<int:pk>/delete', views.ArticleDeleteView.as_view(), name="article_delete"),
    path('file-upload/', views.FileUploadView.as_view(), name="file_upload"),
    path('select-folder/', views.SelectFolderView.as_view(), name="select_folder"),
    path('edit-file/', views.FileEditView.as_view(), name="file_edit"),
    path('search', views.SearchView.as_view(), name="search"),
    path('article-post/<int:pk>/update', views.ArticleUpdateView.as_view(), name="article_update"),
    path('sample/', views.CreateObjectPostView.as_view(), name="test2"),
    

]