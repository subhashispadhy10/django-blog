from django import forms
from blogs_app.models import category

class add_category_form(forms.ModelForm):
     category=forms.CharField(label='Category',widget=forms.TextInput(attrs={
          'class':'form-control m-2'
     }))
     class Meta:
          model=category
          fields=['category']