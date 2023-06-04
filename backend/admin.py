from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'title', 'text', 'company', 'upvotes')
    
admin.site.register(Comment, CommentAdmin)
