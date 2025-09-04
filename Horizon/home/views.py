from django.shortcuts import render
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
