from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User,on_delete=models.CASCADE,null=True) #on_delete=models.CASCADE used to delete all users posts after deleting the user 	
	#body = models.TextField()
	header_image = models.ImageField(null=True,blank=True, upload_to="images/")
	body = RichTextField(blank=True,null=True)
	article_date = models.DateField(auto_now_add=True)

	def __str__(self):
		return self.title + '|' + str(self.author) #author is an object so i need to turn it to a string / this is how the information of the post is shown in the database --> exp:firstpost|nekoula

	def get_absolute_url(self):
		return reverse('home')