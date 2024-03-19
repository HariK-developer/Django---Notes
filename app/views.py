from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer
from rest_framework.response import Response
from rest_framework import status


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.valid_data()
    serializer_class = NoteSerializer
    
    def list(self,*args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        response = {"success": True,"data": serializer.data,"status":status.HTTP_200_OK}
        return Response(response)
    
        
class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.valid_data()
    serializer_class = NoteSerializer
    
    
    def perform_destroy(self, serializer):
        serializer.deleted = True
        serializer.save()
        return 
    