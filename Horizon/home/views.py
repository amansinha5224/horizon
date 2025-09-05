from django.shortcuts import render, HttpResponse, redirect
from .models import Contact
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
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

def handleSignup(request):
    if request.method == 'POST':
        # Get Post Parameters
        username = request.POST['username']
        firstName = request.POST['fname']
        lastName = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        confirmPassword = request.POST['cpassword']

        # Checks
        if len(username) < 3:
            messages.error(request, 'Username is too short')
            return redirect('home')
        if len(username) > 15:
            messages.error(request, 'Username is too long')
            return redirect('home')
        if not username.isalnum():
            messages.error(request, 'Username should not contain special charaters')
            return redirect('home')
        if password != confirmPassword:
            messages.error(request, 'Password do not matched')
            return redirect('home')
        
        # Create the user
        myUser = User.objects.create_user(username, email, password)
        myUser.first_name = firstName
        myUser.last_name = lastName

        myUser.save()

        myUser = authenticate(username = username, password = password)
        if myUser is not None:
            login(request, myUser)
            messages.success(request, f"Register successfully, Welcome! {myUser.first_name} to Horizon blogs")
            return redirect('home')
    
    return HttpResponse("<h1>404 - Not Found</h1>")
    
def handleLogin(request):
    if request.method == 'POST':
        # Get parameters
        username = request.POST['login-username']
        password = request.POST['login-password']

        User = authenticate(username = username, password = password)

        if User is not None:
            login(request, User)
            messages.success(request, f"Welcome! {User.first_name} to Horizon blogs")
            return redirect('home')
        
        else:
            messages.error(request, 'Invaild Credentials, Please try again')
            return redirect('home')

    return HttpResponse("<h1>404 - Not Found</h1>")
    
def handleLogout(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return redirect('home')
