from rest_framework import serializers
from .models import Comment, Company

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('id', 'company_name', 'comment_count', 'upvotes', 'downvotes')

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
       model = Comment
       fields = ('id', 'title', 'user', 'text', 'date', 'company_name', 'upvotes', 'downvotes')  
       