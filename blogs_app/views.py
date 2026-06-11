from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from . models import category,Blog,Comment
from django.db.models import Q
from django.views import View
from . forms import registration_form,login_form
from django.contrib import messages
from django.contrib.auth import login,logout
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
    if request.method == 'POST':
        user=request.user
        cmt=request.POST.get('comment')
        c=Comment(user=user,comment=cmt,blog=slug_post)
        c.save()
        return HttpResponseRedirect(request.path_info)
    comment=Comment.objects.filter(blog=slug_post)
    comment_count=comment.count()
    return render(request,"slug_posts.html",{'slug':slug_post,'comment':comment,'cc':comment_count})

def search(request):
    keyword=request.GET.get('keyword','').strip()
    blog=Blog.objects.filter(Q(title__icontains=keyword) | Q(short_description__icontains=keyword) | Q(blog_body__icontains=keyword))
    
    return render(request,"search.html",{'blog':blog,'keyword':keyword})

class registration(View):
    def get(self,request):
        form=registration_form()
        return render(request,"registration.html",{'form':form})
    def post(self,request):
        form=registration_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration has Completed ")
            return redirect('registration')
        else:
            messages.warning(request,"Not Valid")
        return render(request,"registration.html",{'form':form})

class login_view(View):
    def get(self,request):
        form=login_form()
        return render(request,"login.html",{'form':form})
    def post(self,request):
        form=login_form(request,data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
           
            return redirect('home')
        else:
            messages.warning(request,"Not Valid")
        return render(request,"login.html",{'form':form})


def logout_view(request):
    logout(request)
    messages.success(request,"logout Successfully")
    return redirect('login')