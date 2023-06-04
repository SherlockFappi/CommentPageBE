from django.db import models

class Comment(models.Model):
    title = models.CharField(max_length=80)
    user = models.CharField(max_length=16)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    company = models.CharField(max_length=80)
    upvotes = models.IntegerField()
    
    def __str__(self):
        return '{self.title}:\n{self.text}'
