from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.core import serializers
from django.http import HttpResponse

from django.utils import timezone
from .forms import PostCreateForm

from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.conf import settings
# Create your views here.


def posts(request):
    posts = Post.objects.filter(
        published_at__isnull=False).order_by('-published_at')
    serialized_posts = []
    for post in posts:
        serialized_posts.append(str(JsonResponse(model_to_dict(post)).content))
        
    if settings.DEBUG :
        return render(request, 'blog/posts.html', {'posts': posts, 'full_info': serialized_posts})
    else:
        return render(request, 'blog/posts.html', {'posts': posts})

def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    
    return render(request, 'blog/post_detail.html', {'post': post})

def post_create(request):
    if request.method == "POST":
        form = PostCreateForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_at = timezone.now()
            post.save()
            return redirect('post_detail', id=post.id)
    else:
        form = PostCreateForm()
    return render(request, 'blog/post_create.html', {'form': form})