from django.urls import path
from . import views
 

urlpatterns = [
  path('',views.dash,name='dashboard'),
  path('dash_category/',views.dash_category,name='dash_category'),
  path('add_category/',views.add_category.as_view(),name='add_category'),
  path('edit_category/<int:id>/',views.edit_category,name='edit_category'),
]