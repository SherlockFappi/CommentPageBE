from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CommentSerializer
from .models import Comment

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('date')
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=id', 'user', 'title', 'company']
    ordering_fields = ['id', 'user', 'title', 'company', 'upvotes']
    ordering = ['-date']
    
    @action(methods=['get'], detail=False)
    def newest(self, request):
        newest = self.get_queryset().order_by('date').last()
        serializer = self.get_serializer_class()(newest)
        return Response(serializer.data)
    
    @action(methods=['get'], detail=False)
    def oldest(self, request):
        oldest = self.get_queryset().order_by('date').first()
        serializer = self.get_serializer_class()(oldest)
        return Response(serializer.data)
