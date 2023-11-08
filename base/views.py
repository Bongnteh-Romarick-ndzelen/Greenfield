from django.shortcuts import render, redirect
from .forms import ContactForm, LiveChatForm
from django.contrib import messages
from .models import BlogPost

# Create your views here.


#home page
def index(request):
    BlogPosts = BlogPost.objects.all()
    forms = LiveChatForm(request.POST)
    if forms.is_valid():
        forms.save()
        messages.info(request, " Thank you! We will get back to you shortly!")
        return redirect('/')
    context = {
        'forms':forms,
        'BlogPosts':BlogPosts,
    }
    return render(request, 'index.html', context)

#contact section
def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.info(request, " Thank you! Your message has been submitted. We will get back to you shortly!")
        return redirect('/contact#form')

    context = {
        'form':form,
    }
    return render(request, 'contact.html',context)


#Blog page
def blog(request):
    return render(request, 'blog.html')

