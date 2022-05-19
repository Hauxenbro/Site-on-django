from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from .models import *
from .forms import AddArt, RegUserForm, LoginUserForm, EmailForm
# Create your views here.

def about_auth(request):
    return render(request, 'blog/author.html')

def contact_us(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            return redirect('home')
    else:
        form = EmailForm()
    return render(request, 'blog/email.html', {'form':form})

def logout_user(request):
    logout(request)
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = RegUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
         form = RegUserForm()
    return render(request, 'blog/reguser.html', {'form':form})

def login_user(request):
    if request.method == 'POST':
        form = LoginUserForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = LoginUserForm()
    return render(request, 'blog/loguser.html', {'form':form})



class Home_blog(ListView):
    model = Article
    template_name = 'blog/main_blog.html'
    context_object_name = 'articles'
    extra_context = {'title':'Мой блог'}

    def get_queryset(self):
        return Article.objects.filter(is_published = True)


class Category_view(ListView):
    model = Article
    template_name = 'blog/cat.html'
    context_object_name = 'articles'
    allow_empty = False

    def get_queryset(self):
        return Article.objects.filter(category_id=self.kwargs['category_id'], is_published=True)

class Art_view(DetailView):
    model = Article
    pk_url_kwarg = 'pk'
    template_name = 'blog/art_view.html'
    context_object_name = 'article_item'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views += 1
        self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class AddArticle(CreateView, LoginRequiredMixin):
    form_class = AddArt
    template_name = 'blog/add_article.html'
    success_url = reverse_lazy('home')