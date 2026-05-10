from django.http import HttpResponse
from django.shortcuts import render
from blogs_app.models import category,Blog
from assignment.models import About

def home(request):
    categories=category.objects.all()
    is_feature=Blog.objects.filter(is_featured=True,status='published').order_by('-updated_at')
    recent_post=Blog.objects.filter(is_featured=False,status='published')
   
    about=About.objects.first()
    print(about)
    return render(request,"home.html",{'categories':categories,'featured':is_feature,'posts':recent_post,'about':about})