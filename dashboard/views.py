from django.shortcuts import render,redirect
from blogs_app.models import Blog,category
from django.contrib.auth.decorators import login_required
from . forms import add_category_form
from django.views import View
from django.contrib import messages
from django.utils.decorators import method_decorator


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