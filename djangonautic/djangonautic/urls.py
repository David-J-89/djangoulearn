from django.contrib import admin
from django.urls import path, include
from .import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from articles import views as article_views


urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'accounts/', include('accounts.urls')),
    path(r'articles/', include('articles.urls')),    
    path(r'about/', views.about),
    path(r'', article_views.article_list, name="home"),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
