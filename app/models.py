from django.db import models

# Create your models here.



class  BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True, auto_now_add=False)
    isDelete = models.CharField(max_length=50,default='0')
    
    
    class Meta:
        abstract = True
        ordering = ['-created_at']
        

class Note(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField( max_length=50)
    
    class Meta:
        ordering = ['-created_at']