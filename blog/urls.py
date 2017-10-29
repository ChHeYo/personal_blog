"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import views as auth_views

from personal_blog.views import (
    PostList, PostDetailView,
    PostCreateView, PostUpdateView,
    PostDeleteView, MyLoginView, )

urlpatterns = [
    url(r'^$', PostList.as_view(), name='index'),
    url(r'^login/$', MyLoginView.as_view(), name='login'),
    # url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout'),
    url(r'^create/$', PostCreateView.as_view(), name='create'),
    url(r'^post/(?P<slug>[\w-]+)/$', PostDetailView.as_view(), name='post_detail'),
    url(r'^post/(?P<slug>[\w-]+)/update/$', PostUpdateView.as_view(), name='post_update'),
    url(r'^post/(?P<slug>[\w-]+)/delete/$', PostDeleteView.as_view(), name='post_delete'), 
    url(r'^admin/', admin.site.urls),
]
