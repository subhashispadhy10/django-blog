from django.shortcuts import render,redirect
from . models import category,Blog
from django.db.models import Q
# Create your views here.
def posts(request,id):
    post_id=Blog.objects.filter(status='published',category_blog_id=id)
    try:
       cat_title=category.objects.get(id=id)
    except:
        return redirect('home')
     
    return render(request,"posts_category.html",{'post':post_id,'cat':cat_title})

def slug_blogs(request,slug):
    slug_post=Blog.objects.get(slug=slug,status='published')
    return render(request,"slug_posts.html",{'slug':slug_post})

def search(request):
    keyword=request.GET.get('keyword')
    blog=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
    
    return render(request,"search.html",{'blog':blog,'keyword':keyword})
 
