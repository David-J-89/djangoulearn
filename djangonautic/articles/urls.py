from django.urls import path
from .import views
from django.urls import include, re_path

urlpatterns = [
    path(r'', views.article_list, name="list"),
    re_path(r'^(?P<slug>[\w-]+)/$', views.article_detail)
]