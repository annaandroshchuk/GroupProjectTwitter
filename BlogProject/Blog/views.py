from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import MyUserCreationForm
from .models import Post
from django.contrib.auth import get_user_model

User = get_user_model()


def index(request):
    if request.method == 'POST' and request.user.is_authenticated:
        text = request.POST.get('text')
        image = request.FILES.get('image')
        if text:
            Post.objects.create(author=request.user, text=text, image=image)
            return redirect('index')

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'posts': posts})


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = MyUserCreationForm()

    return render(request, 'register.html', {'form': form})
