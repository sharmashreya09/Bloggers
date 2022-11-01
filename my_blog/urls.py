from django.urls import path
from my_blog import views

urlpatterns = [
    path('',views.index,name="homepage"),
    path('blog/',views.blog,name="blogs"),
    path('blog',views.blog,name="blogs"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('blogpost/<str:slug>',views.blogpost,name='blogpost'),
    path('contact',views.contact,name='contact'),
    path('createblog/',views.createblog,name='createblog'),

]
