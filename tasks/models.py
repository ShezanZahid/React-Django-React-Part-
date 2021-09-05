from django.db import models
from postType.models import PostType

# Create your models here.

class Task(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    image= models.ImageField(upload_to='images/',default="")
    post_type= models.ForeignKey(PostType,default=1,related_name='post_title', on_delete=models.CASCADE)
    post_privacy = models.BooleanField(default=True)
    created_by= models.CharField(default="admin",max_length=100)
    created_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

