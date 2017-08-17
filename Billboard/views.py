from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse
import datetime

from Billboard.models import Post

def index(request):

    latest_post_list = Post.objects.order_by('-pub_date')[:5]
    return render(request, 'Billboard/index.html',  {"posts": latest_post_list})

def newpost(request):
    title = request.POST.get('title')
    author = request.POST.get('author')
    content = request.POST.get('content')
    new_post = Post(title=title, name=author, content=content)
    new_post.save()
    context = {'new_post': new_post}
    return redirect('index')

