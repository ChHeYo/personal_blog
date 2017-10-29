from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.views.generic import (
    ListView, DetailView,
    CreateView, DeleteView,
    UpdateView, )

from .models import Post
from .forms import PostForm, MyLoginForm

# Create your views here.


class MyLoginView(LoginView):
    authentication_form = MyLoginForm
    template_name = 'registration/login.html'


class PostList(ListView):
    '''List of Posts'''
    model = Post
    context_object_name = 'Posts'
    template_name = 'blog/index.html'


class PostDetailView(DetailView):
    '''Detail of a Post'''
    model = Post
    context_object_name = 'post'
    template_name = 'blog/detail.html'


class PostCreateView(CreateView, LoginRequiredMixin):
    '''Creating a new post'''
    model = Post
    form_class = PostForm
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(UpdateView, LoginRequiredMixin):
    '''Update a post'''
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'


class PostDeleteView(DeleteView, LoginRequiredMixin):
    '''Delete a post'''
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('index')
