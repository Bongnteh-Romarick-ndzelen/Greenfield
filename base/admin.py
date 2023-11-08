from django.contrib import admin
from .models import Contact, LiveChat, BlogPost

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ['name','email','number','subject','date_send']
    readonly_fields = ['name', 'email', 'number', 'subject', 'message']
    search_fields = ['name','email','number']
    list_per_page = 10

class LiveChatAdmin(admin.ModelAdmin):
    list_display = ['name','number','send_date']
    readonly_fields = ['name', 'number','message']
    search_fields = ['name','number']
    list_per_page = 5
    
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'image','content','author','date']
    search_fields = ['title', 'content','author']
    list_per_page = 8

admin.site.register(Contact, ContactAdmin)
admin.site.register(LiveChat, LiveChatAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
