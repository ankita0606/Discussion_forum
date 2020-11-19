from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import datetime
from PIL import Image
# Create your models here.
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.png', upload_to='profile_pics')
	followers=models.IntegerField(default=0)
	following=models.IntegerField(default=0)
	questions=models.IntegerField(default=0)
	answers=models.IntegerField(default=0)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self):
		super().save()

		img=Image.open(self.image.path)
		if img.height>300 or img.width>300:
			output_size=(300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Question(models.Model):
	user_posted=models.ForeignKey(Profile,null=True,blank=True,on_delete=models.SET_NULL)
	question_text=models.TextField(null=True ,blank=True)
	vote=models.IntegerField(default=0)
	time_post=models.DateTimeField(auto_now_add=False,default=datetime.datetime.now)
	
	def __str__(self):
		return self.question_text

class Answer(models.Model):
	user_posted=models.ForeignKey(User,null=True,blank=True,on_delete=models.SET_NULL )
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	vote=models.IntegerField(default=0)
	answer_text=models.TextField(null=True ,blank=True)
	time_post=models.DateTimeField(auto_now_add=False,default=datetime.datetime.now)
	

	def __str__(self):
		return self.question.question_text
class Voteofans(models.Model):
	answer= models.ForeignKey(Answer,on_delete=models.CASCADE)
	vote=models.IntegerField(default=0)
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

	def __str__(self):
		return self.vote

class Voteofques(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	vote=models.IntegerField(default=0)
	user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)

	def __str__(self):
		return self.vote