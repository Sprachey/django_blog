from django.contrib import admin
from .models import User,BlogPost

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ['user_id','username','email']
    search_fields = ['username']

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['post_id','title','author']
    list_filter = ["author"]
    

# Register your models here.


admin.site.register(User,UserAdmin)
admin.site.register(BlogPost,BlogPostAdmin)