from django.db import models
from datetime import datetime
from user.models import User

class Group(models.Model):
	""" Main table for Group """
	group_organizer = models.ForeignKey(User)
	group_name = models.CharField(max_length=255)
	group_description = models.TextField(max_length=255, blank=True)
	created_dateTime = models.DateTimeField(auto_now_add=True)

class Group_User(models.Model):
	""" Relationship table for message system and user """
	group_id = models.ForeignKey(Group)
	user_id = models.ForeignKey(User)
	last_message_dateTime = models.DateTimeField(default=datetime.now())

class Message_System_Topic(models.Model):
	""" Topic table for message system """
	group_id = models.ForeignKey(Group)
	originator_id = models.ForeignKey(Group_User)
	topic_name = models.TextField()
	topic_description = models.TextField()
	created_dateTime = models.DateTimeField(auto_now_add=True)

class Message_System_Message(models.Model):
	message_system_topic_id = models.ForeignKey(Message_System_Topic)
	group_user_id = models.ForeignKey(Group_User)
	message = models.TextField()
	created_dateTime = models.DateTimeField(auto_now_add=True)



