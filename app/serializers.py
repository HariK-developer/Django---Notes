from rest_framework import serializers
from .models import Note



class NoteSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Note
        fields = ['id', 'title','content','category','deleted']
    
    
    def create(self, validated_data):
        """
        Create and save a new `Note` instance, given the validated data.
        """
        return Note.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """
        Update and save a new `Note` instance, given the validated data.

        Parameters:
        instance (Note): The instance of the Note to be updated.
        validated_data (dict): The validated data to update the instance with.

        Returns:
        Note: The updated Note instance.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.category = validated_data.get('category', instance.category)
        instance.save()
        return instance
    