from django.urls import path
from . import views

urlpatterns=[
  path('',views.home,name='home'),
  path('add/',views.userpost,name='userpost'),
  path('delete/<int:post_id>/', views.delete, name='delete'),

]