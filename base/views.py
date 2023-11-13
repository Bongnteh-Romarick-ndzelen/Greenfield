from django.shortcuts import render, redirect
from .forms import ContactForm, LiveChatForm, CommentForm
from django.core.paginator import Paginator
from django.contrib import messages
from .models import BlogPost, Comment, Gallery, Team


# Create your views here.


#home page
def index(request):
    team = Team.objects.all()
    paginator = Paginator(team, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #forms = LiveChatForm(request.POST)
    #if forms.is_valid():
        #forms.save()
        #messages.info(request, " Thank you! We will get back to you shortly!")
        #return redirect('/')
    context = {
        'page_obj':page_obj,
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
    BlogPosts = BlogPost.objects.all()[::-1]
    paginator = Paginator(BlogPosts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    coment = Comment.objects.all()[::-1] #method to reverse all the comments
    form1 = CommentForm(request.POST)
    if form1.is_valid():
        form1.save()
        messages.info(request, " Thank you! Comment submitted. It's under review by the Administrator!")
        return redirect('/blog#comment')
    context = {
        'page_obj': page_obj,
        'character_limit': 200,
        'form1': form1,
        'coment':coment,
    }
    return render(request, 'blog.html', context)

#Gallery section
def gallery(request):
    gallery = Gallery.objects.all()[::-1]
    paginator = Paginator(gallery, 8)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'gallery.html', context)

