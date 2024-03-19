from rest_framework import serializers
from .models import Note



class NoteSerializer(serializers.Serializer):
   
    class Meta:
        model = Note
        fields = ['id', 'title','content','category']
    
    
    def create(self, validated_data):
        return Note.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    
    def delete(self, instance):
        instance.isDelete = '1'
        instance.save()
        return 