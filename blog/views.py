from django.shortcuts import render , get_object_or_404, redirect
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

def post_list(request):
    post = Post.objects.filter(is_active=True).order_by('-created_at')
    context = {
        'post': post
    }
    return render(request,'blog/post_list.html',context)

def post_detail(request, slug):
    post = get_object_or_404(Post,slug=slug)
    context = {
        'post': post
    }
    return render(request,'blog/post_detail.html',context)

@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.created_by = request.user
            post.save()
            messages.success(request, 'Post created successfully')
            return redirect('post_list')
    else:
        form = PostForm()
    context = {
        'form': form
    }
    return render(request,'blog/post_create.html',context)