from django.contrib import admin
from blog.models import Blog

class BlogAdmin(admin.ModelAdmin):
    class Media:
        css = {
            "all":("css/main.css",)
        }


        js = ("js/blog.js",)

# Register your models here.
admin.site.register(Blog, BlogAdmin)


