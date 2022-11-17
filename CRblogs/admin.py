from django.contrib import admin
from .models import Contact, Tag, Category, Blog_post, Comment, Extended_user
# for extending user model
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Tag)
admin.site.register(Category)


class Extended_userInline(admin.StackedInline):
    model =Extended_user
    can_delete = False
    verbose_name_plural = 'Extended_Users' 

class CustomizedUserAdmin(UserAdmin):
    inlines = (Extended_userInline, )

admin.site.unregister(User)
admin.site.register(User, CustomizedUserAdmin)

# TO Modify Comment view for admin
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id','name','date','comment_msg','rel_post_id','verified']
    list_editable = ['verified']
admin.site.register(Comment, CommentAdmin)

# To modify Contact view for admin
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id','name','email','subject']
admin.site.register(Contact, ContactAdmin)


# To modify Blog Post view for admin
class Blog_postAdmin(admin.ModelAdmin):
    list_display = ['id','name','date','upload_by']
admin.site.register(Blog_post, Blog_postAdmin)

