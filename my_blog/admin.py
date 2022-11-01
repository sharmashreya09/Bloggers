from django.contrib import admin
from my_blog .models import Blog_detail
from my_blog.models import Contact

# Register your models here.


admin.site.register(Blog_detail)
admin.site.register(Contact)