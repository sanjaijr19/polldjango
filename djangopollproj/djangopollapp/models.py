from django.db import models
from django.contrib.auth.models import User

# Create your models here.
# class User(models.Model):
#     name = models.CharField(max_length=25)
#     email = models.EmailField()
#     password = models.CharField(max_length=20)


class Poll(models.Model):
    title = models.CharField(max_length=30)
    description= models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    end_date = models.DateTimeField('date ended')
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.description




class Choice(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True,blank=True)
    CHOICES = (
        ('1','option 1'),
        ('2,','option 2'),
        ('3,','option 3'),
    )
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choices = models.CharField(max_length=20, choices=CHOICES)




class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    count = models.IntegerField()


