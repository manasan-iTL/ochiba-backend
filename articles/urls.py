from django.urls import path
from articles import views


#app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('article-list/', views.ArticleListView.as_view(), name="article_list"),
    path('article-detail/<int:pk>/', views.ArticleDetailView.as_view(), name="article_detail"),
    path('article-create/', views.ArticleCreateView.as_view(), name="diary_create"),
    path('article-update/<int:pk>/', views.ArticleUpdateView.as_view(), name="article_update"),
    path('article-delete/<int:pk>/', views.ArticleDeleteView.as_view(), name="article_delete"),
]