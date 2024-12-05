from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm

# Create your views here.

# List Blog Posts
def post_list(request):
    posts = BlogPost.objects.all()#.order_by('-created_at')
    #print("I am in post_list")
    return render(request, 'post_list.html', {'posts': posts})

# View Blog Post Details
def post_detail(request, id):
    post = get_object_or_404(BlogPost, id=id)
    return render(request, 'post_detail.html', {'post': post})

# Create Blog Post
def create_post(request):
    if request.method == "POST":
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = BlogPostForm()
    return render(request, 'create_post.html', {'form': form})

# Edit Blog Post
def edit_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == "POST":
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=post.id)
    else:
        form = BlogPostForm(instance=post)
    return render(request, 'edit_post.html', {'form': form})

# Delete Blog Post
def delete_post(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == "POST":
        post.delete()
        return redirect('post_list')
    return render(request, 'delete_post.html', {'post': post})

# Add Comment
def add_comment(request, id):
    post = get_object_or_404(BlogPost, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', id=post.id)
    else:
        form = CommentForm()
    return render(request, 'add_comment.html', {'form': form, 'post': post})

# Edit Comment
def edit_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', id=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'edit_comment.html', {'form': form})

# Delete Comment
def delete_comment(request, id):
    comment = get_object_or_404(Comment, id=id)
    if request.method == "POST":
        comment.delete()
        return redirect('post_detail', id=comment.post.id)
    return render(request, 'delete_comment.html', {'comment': comment})