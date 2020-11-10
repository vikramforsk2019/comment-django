from django.db import models
import os
# Create your models here.
def user_directory_path(instance, filename):
    return '/pic/{0}/{1}'.format(instance.user.id, filename)

class Signup(models.Model):
	name= models.CharField(max_length=30, unique=True)
	uname= models.CharField(max_length=30, unique=True)
	email= models.EmailField(max_length=30, unique=True)
	password=models.CharField(max_length=30)
	pic=models.FileField(upload_to=user_directory_path, default='pic/default.png', null=True, blank=True)
	class Meta:
		db_table="signup"

 	
