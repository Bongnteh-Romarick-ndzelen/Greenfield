from django.contrib import admin
from .models import Contact, LiveChat, BlogPost, Comment, Gallery, Team
from django.utils.html import format_html

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
    
class CommentAdmin(admin.ModelAdmin):
    list_filter = ['situations']
    list_display = ['name', 'comment', 'email', 'send_date','status', '_']
    search_fields = ['name','situations']
    #readonly_fields = ['name', 'comment', 'email', 'send_date']
    list_per_page = 10
    
    #Function to change icons for situations
    def _(self, obj):
        if obj.situations == 'Approved':
            return True
        elif obj.situations == 'Pending':
            return None
        else:
            return False
    _.boolean = True
    
    #Function to color the text
    def status(self, obj):
        if obj.situations == 'Approved':
            color = 'green'
        elif obj.situations == 'Pending':
            color = '#fea95e'
        else:
            color = '#ff0000'
        return format_html("<strong><p style='color:{}'>{}</p></strong>".format(color, obj.situations))
    status.allow_tags = True

class GalleryAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'gallery_image', 'date_posted']
    search_fields = ['title', 'content', 'date_posted']
    list_per_page = 10

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','member_img','position','description']
    search_fields = ['name','member_img', 'position','description']
    list_per_page = 5

admin.site.register(Contact, ContactAdmin)
admin.site.register(LiveChat, LiveChatAdmin)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(Team, TeamAdmin)