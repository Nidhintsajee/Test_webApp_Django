from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone 
# Create your models here.

class User_profile(models.Model):
	user = models.ForeignKey(User,on_delete=models.CASCADE)
	phone_number = models.CharField(max_length=20)
	profile_image = models.ImageField(upload_to='profile_image')
	DOB = models.DateTimeField()

	def __str__(self):
		return self.user.username
