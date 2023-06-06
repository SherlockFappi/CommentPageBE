from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import CommentSerializer, CompanySerializer
from .models import Comment

class CompanyView(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Comment.objects.all().order_by('company_name')

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('date')
    
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['=id', 'user', 'title', 'company_name']
    ordering_fields = ['id', 'user', 'title', 'company_name', 'upvotes', 'downvotes']
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

#TODO Einzelne Attribute der Entität abrufen können
#TODO Einzelne Attribute der Entität patchen können
#TODO Nach spezifischem User suchen können
#TODO Nach spezifischer Firma suchen können
#TODO Einen Kommentar up-und downvoten können
#TODO Kommentare löschen können
#TODO Suche für CompanyName fixen
