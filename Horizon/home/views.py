from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from blog.models import Post
from django.contrib import messages

# Create your views here.
def home(request):
    latestPosts = Post.objects.all().order_by('-timestamp')[:4]
    return render(request, 'home/home.html', {'posts' : latestPosts})

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']

        if(len(name) < 2 or len(email) < 5 or len(phone) < 10 or len(content) < 2):
            messages.error(request, "Please fill the form correctly!")
        else:
            messages.success(request, "Form submitted successfully!")
            contact = Contact(
                name = name,
                phone = phone,
                email = email,
                content = content,
            )

            contact.save()
        
    return render(request, 'home/contact.html')

def search(request):
    query = request.GET.get("query", "").strip()

    if(not query):
        return redirect('home')

    if(len(query) > 70):
        allPost = Post.objects.none()
    else:
        allPostTitle = Post.objects.filter(title__icontains = query)
        allPostContent = Post.objects.filter(content__icontains = query)
        allPostAuthor = Post.objects.filter(author__icontains = query)

        allPost = allPostTitle.union(allPostContent, allPostAuthor)

    params = {'allPost' : allPost, 'query' : query}

    if(len(allPost) == 0):
        messages.warning(request, "No search result found please refine your query")

    return render(request, 'home/search.html', params)