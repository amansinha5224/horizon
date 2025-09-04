from django.shortcuts import render
from .models import Post

# Create your views here.
def blogHome(request):
    allPost = Post.objects.all()

    return render(request, 'blog/blogHome.html', {'allPost' : allPost})

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    return render(request, 'blog/blogPost.html', {'post' : post})
