from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post
# ignore error: %s %r has no %r member 
# pylint: disable = E1101 
# Create your views here.
def post_list(request):
    post_list = Post.objects.filter(published_date__lte=timezone.now()).order_by('-created_date')
    return render(request, 'blog/post_list.html', {'post_list': post_list})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request,'blog/post_detail.html', {'post': post})