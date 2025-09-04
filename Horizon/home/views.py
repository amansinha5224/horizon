from django.shortcuts import render
from .models import Contact

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        phone = request.POST['phone']
        email = request.POST['email']
        content = request.POST['content']

        contact = Contact(
            name = name,
            phone = phone,
            email = email,
            content = content,
        )

        contact.save()
        
    return render(request, 'home/contact.html')
