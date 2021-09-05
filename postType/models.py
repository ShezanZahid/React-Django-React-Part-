from django.db import models

class PostType(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=100)
    details = models.CharField(max_length=100)
    status_type=models.TextChoices('status_type','Active Inactive')
    status = models.CharField(default="Active",choices=status_type.choices, max_length=100)
    created_by= models.CharField(default="admin",max_length=100)
    create_date= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
