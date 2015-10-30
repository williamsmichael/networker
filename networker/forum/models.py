from django.db import models
from django.contrib.auth.models import User
from django.contrib import admin


class Forum(models.Model):
	""" Forum for each group """
	title = models.CharField(max_length=60)

	def __str__(self):
		return self.title
		pyt

class Thread(models.Model):
	""" Threads for the Forum """
	creator = models.ForeignKey(User, blank=True, null=True)
	forum = models.ForeignKey(Forum)

	title = models.CharField(max_length=60)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {}".format(self.creator, self.title)


class Post(models.Model):
	""" Post for each Thread """
	creator = models.ForeignKey(User, blank=True, null=True)
	thread = models.ForeignKey(Thread)

	title = models.CharField(max_length=60)
	body = models.TextField(max_length=10000)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "{} - {} - {}".format(self.creator, self.thread, self.title)

	def short(self):
		return "{} - {}\n{}".format(self.creator, selft.title, self.created.strftime("%b %d, %I:%M %p"))
		short.allow_tags = True



		
    
		
