from django.urls import path
from .import views
from django.urls import include, re_path

app_name='articles'

urlpatterns = [
    path(r'', views.article_list, name="list"),
    path(r'create/', views.article_create, name="create"),
    re_path(r'(?P<slug>[\w-]+)/$', views.article_detail, name="detail"),
]