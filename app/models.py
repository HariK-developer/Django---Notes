from django.db import models

# Create your models here.



class CustomManger(models.Manager):
    
    def valid_data(self,*args, **kwargs):
        return self.get_queryset().filter(deleted=False)
        

class  BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField( auto_now=True,)
    deleted = models.BooleanField(default=False)
    
    
    class Meta:
        abstract = True
        

class Note(BaseModel):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.CharField( max_length=50)
    
    class Meta:
        ordering = ['-created_at']
        
    objects = CustomManger()