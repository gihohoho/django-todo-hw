from django.db import models

# Create your models here.


class Todo(models.Model):
    user = models.ForeignKey("user.User", on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_completed = models.BooleanField(default=False)
    image = models.ImageField(blank=True, null=True)
    
    def __str__(self):
        return self.content
