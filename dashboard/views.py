from django.shortcuts import render,redirect
from blogs_app.models import Blog,category
from django.contrib.auth.decorators import login_required
from . forms import add_category_form,Add_post_form,users_add_form,edit_user_form
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.utils.text import slugify
from django.contrib.auth.models import User


@login_required(login_url='login')
def dash(request):
    category_count=category.objects.all().count()
    blog_count=Blog.objects.all().count()
    return render(request,"dashboard.html",{'cc':category_count,'bc':blog_count})

@login_required(login_url='login')
def dash_category(request):
    if request.GET.get('dlt'):
        dlt_id=request.GET.get('dlt')
        category_id=category.objects.get(id=dlt_id)
        category_id.delete()
        messages.success(request,"Deleted successfully")
        return redirect('dash_category')
    return render(request,"dash_category.html")

@method_decorator(login_required,name='dispatch')
class add_category(View):
    def get(self,request):
      form=add_category_form()
      return render(request,"add_category.html",{'form':form})
    def post(self,request):
      
        form=add_category_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Category added successfully")
            return redirect('add_category')
        return render(request,"add_category.html",{'form':form})


def edit_category(request,id):
    cat_id=category.objects.get(id=id)
    if request.method == 'POST':
        cat_id.category=request.POST.get('category_id')
        cat_id.save()
        messages.success(request,"Edited successfully")
        return redirect('dash_category')
    return render(request,"edit_category.html",{'cat_id':cat_id})

def post(request):
    post=Blog.objects.all()
    if request.GET.get('dlt'):
        dlt_id=request.GET.get('dlt')
        blog=Blog.objects.get(id=dlt_id)
        blog.delete()
        messages.warning(request,"Blog posts deleted")
        return redirect('post')
    return render(request,"post.html",{'post':post})

class add_post(View):
    def get(self,request):
         form=Add_post_form()
         return render(request,"add_post.html",{'form':form})
    def post(self,request):
        form=Add_post_form(request.POST,request.FILES)
        if form.is_valid():
            blog=form.save(commit=False)
            blog.author=request.user
            blog.save()
            title=form.cleaned_data['title']
            blog.slug=slugify(title)+'-'+str(blog.id)
            blog.save()
            messages.success(request,"Blog Posts added Successfully")
            return redirect('post')
        return render(request,"add_post.html",{'form':form})


def edit_post(request,id):
    blog_id=Blog.objects.get(id=id)
    if request.method =='POST':
        blog_id.title=request.POST.get('title')
        blog_id.category_blog_id=request.POST.get('category')
        blog_id.feature_image=request.FILES.get('image')
        blog_id.short_description=request.POST.get('short_desc')
        blog_id.blog_body=request.POST.get('long_desc')
        blog_id.status=request.POST.get('status')
        blog_id.is_featured='feature' in request.POST
        blog_id.author=request.user
        blog_id.slug=slugify(blog_id.title)+"-"+str(blog_id.id)
        blog_id.save()
        messages.success(request,"blog Posts updated successfully")
        return redirect('post')
    return render(request,"edit_post.html",{'blog':blog_id})


def users(request):
    users=User.objects.all()
    if request.GET.get('dlt'):
        dlt_id=request.GET.get('dlt')
        user_id=User.objects.get(id=dlt_id)
        user_id.delete()
        messages.warning(request,"User data is Deleted")
        return redirect('users')
    return render(request,"users.html",{'users':users})

class add_users(View):
    def get(self,request):
        form=users_add_form()
        return render(request,"add_users.html",{'form':form})
    def post(self,request):
        form=users_add_form(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Users added successfully")
            return redirect('users')
        return render(request,"add_users.html",{'form':form})

class edit_users(View):
     def get(self,request,id):
       user_id=User.objects.get(id=id)
       form=edit_user_form(instance=user_id)
       return render(request,"edit_users.html",{'form':form})
     def post(self,request,id):
         user_id=User.objects.get(id=id)
         form=edit_user_form(request.POST,instance=user_id)
         if form.is_valid():
             form.save()
             messages.success(request,"Edited Successfully")
             return redirect('users')
         return render(request,"edit_users.html",{'form':form})
     
