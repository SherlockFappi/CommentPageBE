from django.contrib import admin
from .models import Comment, Company

class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'title', 'text', 'company_name', 'upvotes', 'downvotes')

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'comment_count', 'upvotes', 'downvotes')
    
admin.site.register(Comment, CommentAdmin)
admin.site.register(Company, CompanyAdmin)
