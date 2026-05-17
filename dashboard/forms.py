from django import forms
from blogs_app.models import category,Blog
from django.contrib.auth.models import User
from django.utils.text import slugify

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
