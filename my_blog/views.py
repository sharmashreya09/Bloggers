from django.shortcuts import render,HttpResponse
from my_blog.models import Blog_detail
from my_blog.models import Contact
# Create your views here.
def index(request):
    return render(request,'index.html')
def blog(request):
    if request.method == 'POST':
        first_name = request.POST['Firstname']
        last_name = request.POST['Lastname']
        title = request.POST['title']
        content = request.POST['content']
        slug = request.POST['slug']
        email = request.POST['email']
        blog_obj = Blog_detail.objects.create(Firstname=first_name, email=email, title=title, content=content,
                                              slug=slug, Lastname=last_name)

    blogs = Blog_detail.objects.all()
    cntext = {'blogs': blogs}
    return render(request, 'blog.html', cntext)





def about(request):
    return render(request,'about.html')

def blogpost(request,slug):
    blog = Blog_detail.objects.get(slug=slug)
    context = {'blog':blog}
    return render(request ,'blogpost.html',context)

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        contact = Contact.objects.create(name=name, email=email, message=message)

    return render(request, 'contact.html')

def createblog(request):
    return render(request,'createblog.html')





