from django.db import models
import os
# Create your models here.
def user_directory_path(instance, filename):
    return '/pic/{0}/{1}'.format(instance.user.id, filename)

class Health_data(models.Model):
	userid=models.IntegerField()
	group= models.CharField(max_length=30)
	age= models.IntegerField()
	weight=models.IntegerField()
	postfile=models.FileField()
	class Meta:
		db_table="health_data" 	
