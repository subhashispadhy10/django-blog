from django.shortcuts import render,redirect
from . models import category,Blog

# Create your views here.
def posts(request,id):
    post_id=Blog.objects.filter(status='published',category_blog_id=id)
    try:
       cat_title=category.objects.get(id=id)
    except:
        return redirect('home')
     
    return render(request,"posts_category.html",{'post':post_id,'cat':cat_title})
 
