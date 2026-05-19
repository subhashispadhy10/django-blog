from django.db import models
from django.contrib.auth.models import User
 

class category(models.Model):
    category=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)


    class Meta:
        verbose_name_plural='Categories'
    
    def __str__(self):
        return self.category


class Blog(models.Model):
    status_choice=(
    ('draft',"Draft"),
    ('published',"Published")
)
    title=models.CharField(max_length=50)
    slug=models.SlugField(max_length=150,unique=True,blank=True)
    category_blog=models.ForeignKey(category,on_delete=models.CASCADE)
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    feature_image=models.ImageField(upload_to='blog_images/',blank=True)
    short_description=models.TextField(max_length=150)
    blog_body=models.TextField()
    status=models.CharField(choices=status_choice,default='draft')
    is_featured=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
         return self.title

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog=models.ForeignKey(Blog,on_delete=models.CASCADE)
    comment=models.TextField(max_length=250)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
            return self.comment