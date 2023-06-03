from django.contrib import admin
from .models import Comment

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'title', 'text')
    
admin.site.register(Comment, CommentAdmin)
