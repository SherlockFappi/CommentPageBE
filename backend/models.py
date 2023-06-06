from django.db import models

class Company(models.Model):
    company_name = models.CharField(max_length=80, default='')
    comment_count = models.IntegerField(default=0)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.company_name


class Comment(models.Model):
    title = models.CharField(max_length=80)
    user = models.CharField(max_length=16)
    text = models.TextField()
    date = models.DateTimeField(auto_now=True)
    #company = models.CharField(max_length=80)
    company_name = models.ForeignKey(Company, default='', on_delete=models.CASCADE)
    upvotes = models.IntegerField(default=0)
    downvotes = models.IntegerField(default=0)
    
    def __str__(self):
        return '{self.title}:\n{self.text}'
    
#TODO Counter für Comments
