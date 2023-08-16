from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from django.shortcuts import get_object_or_404,render,redirect
from blog.forms import CommentForm
# Create your views here.
def index(request):
  posts = Post.objects.all()
  return render(request,"blog/index.html",{"post":posts})

def post_detail(request,slug):
  if request.user.is_active:

    if request.method == "POST":
      comment_form = CommentForm(request.form)

      if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.content_object = post
        comment.creator = request.user
        comment.save()
        return redirect(request.path_info)
    else:
      comment_form = CommentForm()
  else:
    comment_form = None
  return render(request,"blog/post-detail.html",{"post":post,"comment_from":comment_form})

def post_table(request):
  return render(request,"blog/post-table.html")