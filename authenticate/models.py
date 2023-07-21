from django.db import models
from django.contrib.auth.models import User

# class department(models.Model):
#     pass
# class registration(models.Model):
#     first_name=models.CharField(max_length=100,default='')
#     last_name=models.CharField(max_length=100,default='')
#     username=models.CharField(max_length=100,default='')
#     email=models.EmailField(blank=False,default='')
#     password=models.CharField(max_length=50,blank=False,default='')
#     def __str__(self):
#         return self.username
class to_do_list(models.Model):
    compeltion=(('Completed','Completed'),
                ('NotCompleted','Not Completed'),
                ('InProgress','In Progress'),)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    Tittle=models.CharField(max_length=50)
    to_do_list=models.TextField(default='',verbose_name='Description')
    completed=models.CharField(max_length=50,choices=compeltion,default='c')


    def __str__(self):
        return self.Tittle
    