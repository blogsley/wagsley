from django.shortcuts import render, get_object_or_404
from django.utils import timezone
# from django.contrib.auth.models import User
from accounts.models import User
#from .models import Post
from .forms import ContactForm, ProfileEditForm

def index(request):
    #posts = Post.objects.filter(last_published_at__lte=timezone.now()).order_by('last_published_at')
    posts = []
    return render(request, 'home/index.html', {'posts': posts})

'''
def blog(request):
    posts = Post.objects.filter(last_published_at__lte=timezone.now()).order_by('last_published_at')
    return render(request, 'blog/blog.html', {'posts': posts})
'''

def about(request):
    return render(request, 'home/about.html')

def contact(request):
    return render(request, 'home/contact.html', {'form': ContactForm})

'''
def post(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, 'blog/post.html', {'post': post})
'''

'''
def profile(request, username):
    profile = get_object_or_404(User, username=username)
    posts = Post.objects.filter(owner=profile)
    return render(request, 'home/profile.html', {'profile': profile, 'posts': posts})

def profile_edit(request, username):
    profile = get_object_or_404(User, username=username)
    return render(request, 'home/profile_edit.html', {'profile': profile, 'form': ProfileEditForm})
'''