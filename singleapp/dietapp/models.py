from django.db import models
import os
# Create your models here.
class Signup(models.Model):
	name= models.CharField(max_length=30, unique=True)
	uname= models.CharField(max_length=30, unique=True)
	email= models.EmailField(max_length=30, unique=True)
	password=models.CharField(max_length=30)
	pic=models.FileField()
	class Meta:
		db_table="signup"

class Health_data(models.Model):
	userid=models.IntegerField()
	group= models.CharField(max_length=30)
	age= models.IntegerField()
	weight=models.IntegerField()
	postfile=models.FileField()
	class Meta:
		db_table="health_data" 	