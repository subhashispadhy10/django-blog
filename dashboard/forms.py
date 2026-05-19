from django import forms
from blogs_app.models import category,Blog
from django.contrib.auth.models import User,Permission
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm

class add_category_form(forms.ModelForm):
     category=forms.CharField(label='Category',widget=forms.TextInput(attrs={
          'class':'form-control m-2'
     }))
     class Meta:
          model=category
          fields=['category']

class Add_post_form(forms.ModelForm):
     title=forms.CharField(label='Title',widget=forms.TextInput(attrs={
          'class':'form-control'
     }))
     feature_image=forms.ImageField(label='Image',required=False,widget=forms.ClearableFileInput(attrs={
          'class':'form-control'
     }))
     category_blog=forms.ModelChoiceField(queryset=category.objects.all(),label='Category',widget=forms.Select(attrs={
          'class':'form-select'
     })) 
     short_description=forms.CharField(label='Short Description',max_length=150,widget=forms.Textarea(attrs={
          'class':'form-control','rows':3
     }))
     blog_body=forms.CharField(label='Body Description',widget=forms.Textarea(attrs={
          'class':'form-control','rows':6
     }))
     status=forms.ChoiceField(label='Status',choices=Blog.status_choice,widget=forms.Select(attrs={
          'class':'form-select'
     }))
     feature=forms.BooleanField(label='Feature',required=False,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     })) 

     

     class Meta:
          model=Blog
          fields=['title','category_blog','feature_image','short_description','blog_body','status','feature']

class users_add_form(UserCreationForm):
     username=forms.CharField(label='Username',widget=forms.TextInput(attrs={
          'class':'form-control'
     }))
     email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={
          'class':'form-control'
     }))
     is_active=forms.BooleanField(label="Active",initial=True,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     }))
     is_staff=forms.BooleanField(label='Staff',required=False,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     }))
     is_superuser=forms.BooleanField(label='Superuser',required=False,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     }))
     password1=forms.CharField(label='Password',required=True,widget=forms.PasswordInput(attrs={
          'class':'form-control'
     }))
     password2=forms.CharField(label='Confirm Password',required=True,widget=forms.PasswordInput(attrs={
          'class':'form-control'
     }))
     user_permissions = forms.ModelMultipleChoiceField(
    queryset=Permission.objects.all().order_by('content_type__app_label', 'codename'),
    required=False,
    widget=forms.SelectMultiple(attrs={
        'class': 'form-select',
        'size': '10'   # shows 10 rows and fits nicely in the form
    })
)
     class Meta:
          model=User
          fields=['username','email','is_active','is_staff','is_superuser','password1','password2','user_permissions']

class edit_user_form(forms.ModelForm):
     username=forms.CharField(label='Username',widget=forms.TextInput(attrs={
          'class':'form-control'
     }))
     email=forms.CharField(label='Email',widget=forms.EmailInput(attrs={
          'class':'form-control'
     }))
     is_active=forms.BooleanField(label="Active",initial=True,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     }))
     is_staff=forms.BooleanField(label='Staff',required=False,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     }))
     is_superuser=forms.BooleanField(label='Superuser',required=False,widget=forms.CheckboxInput(attrs={
          'class':'form-check-input'
     }))
     user_permissions = forms.ModelMultipleChoiceField(
    queryset=Permission.objects.all().order_by('content_type__app_label', 'codename'),
    required=False,
    widget=forms.SelectMultiple(attrs={
        'class': 'form-select',
        'size': '10'   # shows 10 rows and fits nicely in the form
    })
)
     class Meta:
          model=User
          fields=['username','email','is_active','is_staff','is_superuser','user_permissions']
       