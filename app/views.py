from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework import filters


class NoteList(generics.ListCreateAPIView):
    search_fields = ['title','category']
    filter_backends = (filters.SearchFilter,)
    queryset = Note.objects.valid_data()
    serializer_class = NoteSerializer
    
    
    
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.valid_data()
    serializer_class = NoteSerializer
    
    
    def perform_destroy(self, serializer):
        serializer.deleted = True
        serializer.save()
        return 
    